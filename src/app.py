from setup.setup import setup
from flask_cors import CORS

from services.chatbot.Pipeline_Model import train

from flask import Flask

from routes.admin import admin_bp
from routes.chatbot import chatbot_bp
from routes.server import server_bp

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.register_blueprint(admin_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(server_bp)

@app.errorhandler(Exception)
def handle_exception(e):
    return {'error': str(e)}


if __name__ == '__main__':
    train()
    app.run()
