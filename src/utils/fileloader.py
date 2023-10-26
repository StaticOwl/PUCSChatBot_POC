import os
from dotenv import load_dotenv

print(load_dotenv("src/.env"))

def print_env():
    print(os.getenv("URL_LIST_PATH"))
