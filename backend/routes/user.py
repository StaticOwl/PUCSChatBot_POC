from flask import Blueprint, request
from flask_cors import cross_origin

from backend.services.user import user


user_bp = Blueprint('user_bp', __name__)


@cross_origin(methods=['POST'])
@user_bp.route('/v1/app/register', methods=['POST'])
def register():
    request_data = request.get_json()
    name = request_data.get('name')
    email = request_data.get('email')
    password = request_data.get('password')

    id = user.register_user(name, email, password)

    return {'id': id, 'email': email}


@cross_origin(methods=['POST'])
@user_bp.route('/v1/app/login', methods=['POST'])
def login():
    request_data = request.get_json()

    is_guest = request_data.get('is_guest', False)
    email = request_data.get('email', '')
    password = request_data.get('password', '')

    result = user.login(is_guest, email, password)
    return result, 200, {'Set-Cookie': f"id={result['id']}"}