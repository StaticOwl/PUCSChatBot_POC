from flask import Blueprint, request

from backend.services.db import db

db_bp = Blueprint('db_bp', __name__)


@db_bp.route('/v1/admin/db/connection_test')
def test_conn():
    db.test_conn()
    return "Success", 200


@db_bp.route('/v1/admin/db/setup_test')
def test_setup():
    result = db.test_setup()
    return {"users": result}, 200


@db_bp.route('/v1/admin/db/setup')
def setup_database():
    db.setup_database()
    return "Success", 200


@db_bp.route('/v1/admin/db/clear')
def clear_database():
    db.clear_database(request.args.get("resetup", "True").lower().strip() == "true")
    return "Success", 200


@db_bp.route('/v1/admin/db/execute')
def execute_query():
    request_data = request.get_json()
    result = db.execute_query(request_data.get("query", ""))
    return result, 200
