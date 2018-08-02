from app.api import bp
from flask import jsonify
from app.models import User


@bp.route('/users', methods=['GET'])
def get_users():
    pass


@bp.route('/users', methods=['POST'])
def create_user():
    return


@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())


@bp.route('/users/<int:id>', methods=['GET'])
def update_user(id):
    pass


@bp.route('/users/<int:id>/tasks', methods=['GET'])
def get_user_tasks():
    pass


@bp.route('/users/<int:id>/tasks', methods=['POST'])
def create_user_task():
    pass


@bp.route('/users/<int:id>/tasks/<int:tid>', methods=['GET'])
def get_user_task(id, tid):
    pass


@bp.route('/users/<int:id>/tasks/<int:tid>', methods=['GET'])
def update_user_task(id, tid):
    pass
