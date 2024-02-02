from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

answerer = "deepset/roberta-base-squad2"

class CreateException(Exception):
    pass

def answer_question_from_context(context, question):
    try:
        qa_pipeline = pipeline('question-answering', model=answerer, tokenizer=answerer)
        input = {
            'question': question,
            'context': context
        }
        res = qa_pipeline(input)['answer']
        return res
    except Exception as e:
        raise CreateException("Error whilst querying Q&A model.\n" + str(e))
