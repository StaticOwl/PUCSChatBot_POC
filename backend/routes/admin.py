from flask import Blueprint

from backend.services.chatbot.palm_model import train

admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route('/v1/admin/chatbot/train', methods=['POST'])
def train_chatbot():
    train()
    return "Success", 200
