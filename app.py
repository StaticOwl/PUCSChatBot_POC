from backend.services.chatbot.Pipeline_Model import train
from backend.routes.runner import app

if __name__ == '__main__':
    train()
    app.run()

    # utils.load_env()
    # data.scrapping.main()