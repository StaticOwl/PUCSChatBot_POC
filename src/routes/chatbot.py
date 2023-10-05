from flask import Blueprint

from services.chatbot import chat as cbchat

chatbot_bp = Blueprint('chatbot_bp', __name__)


@chatbot_bp.route('/v1/chatbot/chat', methods=['POST'])
def chat():
    return {'response': cbchat.chat()}, 200
