from backend.services.chatbot.Pipeline_Model import train
from backend.setup.setup import setup
import argparse
from backend.routes.runner import app


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', '-t', action='store_true', help='train the model')
    parser.add_argument('--setup', '-s', action='store_true', help='setup the project')

    args = parser.parse_args()

    if args.setup:
        setup()
    else:
        train()
        app.run()
