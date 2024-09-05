from flask_restful import Resource, reqparse
from app.models import User, db

user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True)
user_parser.add_argument('email', type=str, required=True)
user_parser.add_argument('password', type=str, required=True)

class UserResource(Resource):
    def get(self, id):
        user = User.query.get_or_404(id)
        return {'id': user.id, 'username': user.username, 'email': user.email}

    def put(self, id):
        args = user_parser.parse_args()
        user = User.query.get_or_404(id)
        user.username = args['username']
        user.email = args['email']
        user.password = args['password']
        db.session.commit()
        return {'message': 'User updated successfully'}

    def delete(self, id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [{'id': u.id, 'username': u.username, 'email': u.email} for u in users]

    def post(self):
        args = user_parser.parse_args()
        user = User(username=args['username'], email=args['email'], password=args['password'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201
