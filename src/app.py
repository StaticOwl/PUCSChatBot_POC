from setup.setup import setup

if not setup():
        raise Exception("Setup failed")

from flask import Flask

from routes.admin import admin_bp
from routes.chatbot import chatbot_bp
from routes.server import server_bp

app = Flask(__name__)
app.register_blueprint(admin_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(server_bp)

@app.errorhandler(Exception)
def handle_exception(e):
    return {'error': str(e)}


if __name__ == '__main__':
    app.run()
