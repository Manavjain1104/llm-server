# from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

# answerer = pipeline('question-answering', model="deepset/roberta-base-squad2", tokenizer="deepset/roberta-base-squad2")


# class QuestionException(Exception):
#     pass


# def answer_question_from_context(context, question):
#     try:
#         print("Begin answering question")
#         print(context)
#         print(question)
#         input = {
#             'question': question,
#             'context': context
#         }
#         print(input)
#         res_no_a = qa_pipeline(input)
#         print(res_no_a)
#         res = res_no_a['answer']
#         return res
#     except KeyboardInterrupt:
#         return "Interrupted"
#     except BaseException as e:
#         raise QuestionException("Error whilst querying Q&A model.\n" + str(e))
