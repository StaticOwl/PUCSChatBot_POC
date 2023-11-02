# pip install langchain
# pip install huggingface_hub
# pip install faiss-cpu
# pip install sentence_transformers

from langchain.document_loaders import TextLoader
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub
import textwrap
import pickle

def train(id,data):
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = id
    loader = TextLoader(data)
    document = loader.load()

    def wrap(text, width=110):
        lines = text.split("\n")
        wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
        wrapped_text = "\n".join(wrapped_lines)
        return wrapped_text

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(document)

    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.8, "max_length": 512})
    chain = load_qa_chain(llm, chain_type="stuff")

    return db, chain


def test(db, chain):
    while True:
        # Get user input
        queryText = input("Ask your question (type 'exit' to quit): ")

        # Check if the user wants to exit
        if queryText.lower() == 'exit':
            print("Exiting the chatbot. Goodbye!")
            break

        # Perform similarity search and retrieve documents
        docsResult = db.similarity_search(queryText)
        docsResult = docsResult[:-1]

        # Get chatbot response
        chatbot_response = chain.run(input_documents=docsResult, question=queryText,raw_response=True)

        # Print chatbot response
        print("Chatbot Response:", chatbot_response)
        

def save_db_and_chain(db, chain, db_filename, chain_filename):
    try:
        with open(db_filename, 'wb') as db_file:
            pickle.dump(db, db_file)
        with open(chain_filename, 'wb') as chain_file:
            pickle.dump(chain, chain_file)
        print(f"db and chain saved successfully to '{db_filename}' and '{chain_filename}'.")
    except Exception as e:
        print(f"Error occurred: {e}")


def load_db_and_chain(db_filename, chain_filename):
    try:
        with open(db_filename, 'rb') as db_file:
            db = pickle.load(db_file)
        with open(chain_filename, 'rb') as chain_file:
            chain = pickle.load(chain_file)
        print(f"db and chain loaded successfully from '{db_filename}' and '{chain_filename}'.")
        return db, chain
    except Exception as e:
        print(f"Error occurred: {e}")
        return None, None



# Usage example:
# db, chain = train("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","faculty_data.txt")
# save_db_and_chain(db, chain,'db.pkl', 'chain.pkl')
# db, chain = load_db_and_chain('db.pkl', 'chain.pkl')
# test(db, chain)