from flask import Blueprint

server_bp = Blueprint('server_bp', __name__)


@server_bp.route('/health', methods=['GET'])
def health():
    return {'status': 'UP'}, 200
