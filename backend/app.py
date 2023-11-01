from services.chatbot.Pipeline_Model import train
from setup.setup import setup
from services.data import scrapping
import argparse
from routes.runner import app
from dotenv import load_dotenv


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', '-t', action='store_true', help='train the model')
    parser.add_argument('--setup', '-s', action='store_true', help='setup the project')
    parser.add_argument('--scraping', '-sc', action='store_true', help='scraping the data from list of urls')

    args = parser.parse_args()
    load_dotenv()
    if args.setup:
        setup()
    elif args.scraping:
        scrapping.run()
    else:
        train()
        app.run()
