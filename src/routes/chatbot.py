from flask import Blueprint
from flask_cors import cross_origin
from services.chatbot import chat as cbchat

chatbot_bp = Blueprint('chatbot_bp', __name__)

@cross_origin
@chatbot_bp.route('/v1/chatbot/chat', methods=['POST'])
def chat():
    return {'response': cbchat.chat()}, 200
