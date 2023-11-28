from flask import Blueprint, request
from flask_cors import cross_origin

from backend.routes.user import USER_ID_COOKIE
from backend.services.chatbot import chat as cbchat

chatbot_bp = Blueprint('chatbot_bp', __name__)


@cross_origin
@chatbot_bp.route('/v1/chatbot/chat', methods=['POST'])
def chat():
    user_id = request.cookies.get(USER_ID_COOKIE, 'N/A')

    request_data = request.get_json()
    user_msg = request_data.get('user_msg', '')

    return {'response': cbchat.chat(user_msg, user_id=user_id)}, 200
