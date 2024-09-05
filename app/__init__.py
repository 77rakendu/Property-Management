# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from config import Config

db = SQLAlchemy()
migrate = Migrate()
api = Api()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    from app.resources.property import PropertyResource, PropertyListResource
    from app.resources.user import UserResource, UserListResource
    from app.resources.booking import BookingResource, BookingListResource
    from app.resources.payment import PaymentResource, PaymentListResource

    api.add_resource(PropertyListResource, '/properties')
    api.add_resource(PropertyResource, '/properties/<int:id>')
    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<int:id>')
    api.add_resource(BookingListResource, '/bookings')
    api.add_resource(BookingResource, '/bookings/<int:id>')
    api.add_resource(PaymentListResource, '/payments')
    api.add_resource(PaymentResource, '/payments/<int:id>')

    return app
