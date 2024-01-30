from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

answerer = "deepset/roberta-base-squad2"

def answer_question_from_context(context, question):
    qa_pipeline = pipeline('question-answering', model=answerer, tokenizer=answerer)
    input = {
        'question': question,
        'context': context
    }
    res = qa_pipeline(input)['answer']

    return res

print(answer_question_from_context(
    "work in a school with student of ages 11 - 16 (secondary school) \
teaching range of stem subjects \
(ass) permenant position \
(good at mario kart) \
experience working with children especially early teenagers \
strong at math, lots of experience with computer programming \
learning entirely stem subject for the past 6 years (and doing longer than that) \
i am personable, good at handling work place conflicts \
(soft wishes) \
in london area \
preferably close to public transport \
school with good reviews (ofsted schools) \
reasonably good pay \
\
(day-to-day) \
going in every week day \
teaching variety of stem subject (math science computing etc) \
lunch duty, monitoring the general community behaviour and welfare (ex timetable ) \
making lessons, and marking work, with enough reason to have time for yourself in the evening",
"What job is suggested?"))