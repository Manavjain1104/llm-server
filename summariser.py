# pip install -U sentence-transformers requests numpy
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

summariser = pipeline("summarization", model="Falconsai/text_summarization")
embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')

MAX_LEN = 250
MIN_LEN = 30


class SummaryException(Exception):
    pass

class EmbeddingException(Exception):
    pass

class BulkEmbeddingException(Exception):
    pass


def create_summary(text: str) -> type[str | SummaryException]:
    try:
        summariser_output = summariser(
            text, min_length=MIN_LEN, do_sample=False
        )
        summary = summariser_output[0]['summary_text']
        return summary
    except BaseException as e:
        raise SummaryException("Error whilst creating summary.\n" + str(e))

# create one vector embedding given a description in form of a string
# example: create_embedding("some job")

def create_embedding(description: str) -> type[List[float] | EmbeddingException]:
    try:
        embedding = embedder.encode([description])
        embedding_normalised = embedding / \
            np.linalg.norm(embedding, axis=1, keepdims=True)
        return embedding_normalised[0].tolist()
    except BaseException as e:
        raise EmbeddingException("Error whilst creating embedding.\n" + str(e))



# create a list of vector embeddings given a list of descriptions
def bulk_create_embeddings(descriptions: List[str]) -> type[List[List[float]] | BulkEmbeddingException]:
    try:
        embeddings = embedder.encode(descriptions)
        embeddings_normalised = embeddings / \
            np.linalg.norm(embeddings, axis=1, keepdims=True)
        return list(map(lambda e: e.tolist(), embeddings_normalised))
    except BaseException as e:
        raise BulkEmbeddingException("Error whilst creating bulk embeddings.\n" + str(e))

if __name__ == "__main__":
    print(create_summary("This is a test"))
    print(create_embedding("This is a test"))
    print(bulk_create_embeddings(["This is a test", "This is another test"]))
