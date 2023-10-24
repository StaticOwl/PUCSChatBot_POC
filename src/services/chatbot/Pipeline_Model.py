from transformers import pipeline

def train(model_id):
  train_output = pipeline("question-answering", model=model_id)
  return train_output

def test(data_file, max_answer_len,train_output):
    with open(data_file, 'r') as file:
        context = file.read()

    while True:
        # Ask a question
        question = input("Ask a question (type 'exit' to quit): ")

        if question.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'

        # Perform question-answering
        answer = train_output(question=question, context=context, max_answer_len=max_answer_len)

        print(f"Question: {question}")
        print(f"Answer: {answer['answer']}")

#Examples
# tqa=train("deepset/tinyroberta-squad2")
# test("faculty_data.txt",50,tqa)

