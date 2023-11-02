# from .Pipeline_Model import test
from .Google import test, load_db_and_chain

db, chain = load_db_and_chain('D:/projects/PFW/590_DL/PFW_ChatBot/backend/services/chatbot/db.pkl',
                              'D:/projects/PFW/590_DL/PFW_ChatBot/backend/services/chatbot/chain.pkl')
def chat(msg, *args, **kwargs):
    return test(msg, db, chain)
