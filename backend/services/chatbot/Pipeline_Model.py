from typing import Callable

from transformers import pipeline

train_output: (Callable | None) = None

def train(model_id="deepset/tinyroberta-squad2"):
    global train_output
    train_output = pipeline("question-answering", model=model_id)

def test(question, data_file="backend/resources/faculty_data.txt", max_answer_len=50):
    with open(data_file, 'r') as file:
        context = file.read()

    answer = train_output(question=question, context=context, max_answer_len=max_answer_len)

    return answer['answer']
        

# #Examples
# tqa=train("deepset/tinyroberta-squad2")
# test("faculty_data.txt",50,tqa)
