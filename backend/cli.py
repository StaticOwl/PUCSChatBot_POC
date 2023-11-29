from services.chatbot.palm_model import test

if __name__ == '__main__':
    import sys
    sys.path.append('.')


    while True:
        query = input("Ask a question (type 'exit' to stop): ")

        if query.lower().strip() == 'exit':
            print("Exiting the loop. Goodbye!")
            break

        response, accuracy = test(query)
        print(f"{response} <[[accuracy = {accuracy}]]>")
