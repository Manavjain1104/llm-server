from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

answerer = "deepset/roberta-base-squad2"

def answer_question_from_context(context, question):
    qa_pipeline = pipeline('question-answering', model=answerer, tokenizer=answerer)
    input = {
        'question': question,
        'context': context
    }
    print(input)
    res = qa_pipeline(input)['answer']

    return res
