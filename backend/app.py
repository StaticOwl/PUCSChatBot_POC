import argparse

if __name__ == '__main__':
    import sys
    sys.path.append('.')

    parser = argparse.ArgumentParser()
    parser.add_argument('--train', '-t', action='store_true', help='train the model')
    parser.add_argument('--setup', '-s', action='store_true', help='setup the project')
    parser.add_argument('--scraping', '-sc', action='store_true', help='scraping the data from list of urls')

    args = parser.parse_args()
    if args.setup:
        from setup.setup import setup
        setup()
    elif args.scraping:
        from services.data import scrapping
        from dotenv import load_dotenv
        load_dotenv()
        scrapping.run()
    else:
        from services.chatbot.pipeline_model import train
        from dotenv import load_dotenv
        from routes.runner import app
        load_dotenv()
        train()
        app.run()
