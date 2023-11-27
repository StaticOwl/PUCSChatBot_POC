import os
import dill

from backend.services.chatbot.palm_model import test

DEFAULT_THRESHOLD = os.environ['PALM_THRESHOLD']
DEFAULT_DB_DILL_PATH = 'backend/resources/db.dill'
DEFAULT_CHAIN_DILL_PATH = 'backend/resources/chain.dill'

with open(DEFAULT_DB_DILL_PATH, "rb") as f:
    db = dill.load(f)
with open(DEFAULT_CHAIN_DILL_PATH, "rb") as f:
    chain = dill.load(f)

while True:
    query = input("Ask a question (type 'exit' to stop): ")

    if query.lower().strip() == 'exit':
        print("Exiting the loop. Goodbye!")
        break

    test(db, chain, THRESHOLD)