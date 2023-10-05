from flask import Flask

from admin.api import admin_bp
from chatbot.api import chatbot_bp
from server.api import server_bp

app = Flask(__name__)
app.register_blueprint(admin_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(server_bp)

@app.errorhandler(Exception)
def handle_exception(e):
    return {'error': str(e)}


if __name__ == '__main__':
    app.run()
