from flask import Blueprint

admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route('/v1/admin/chatbot/train', methods=['POST'])
def train():
    raise Exception('Not Implemented...')
