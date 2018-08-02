from app.api import bp
from flask import jsonify
from app.models import User
from flask import request
from app import db
from flask import url_for


@bp.route('/users', methods=['GET'])
def get_users():
    pass


@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data or 'password' not in data:
        # TODO: return api friendly bad request here
        # must include username, email and password fields
        pass
    if User.query.filter_by(username=data['username']).first():
        # TODO: return api friendly bad request here
        # please use a different username
        pass
    if User.query.filter_by(username=data['email']).first():
        # TODO: return api friendly bad request here
        # please use a different email
        pass
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response


@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())


@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json() or {}
    # TODO: add some authentication here
    if 'username' not in data or 'email' not in data or 'password' not in data:
        # TODO: return api friendly bad request here
        # must include username, email and password fields
        pass
    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())


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
