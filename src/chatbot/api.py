from flask import Blueprint

chatbot_bp = Blueprint('chatbot_bp', __name__)


@chatbot_bp.route('/v1/chatbot/chat', methods=['POST'])
def chat():
    return {'response': "Hardcoded response..."}, 200
