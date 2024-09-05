from flask import Blueprint
from flask_restful import Api
from app.resources.user import UserResource, UserListResource
from app.resources.booking import BookingResource, BookingListResource
from app.resources.property import PropertyResource, PropertyListResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Register User resources
api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:id>')
# Register Booking resources
api.add_resource(BookingListResource, '/bookings')
api.add_resource(BookingResource, '/bookings/<int:id>')

# Register Property resources
api.add_resource(PropertyListResource, '/properties')
api.add_resource(PropertyResource, '/properties/<int:id>')

def init_app(app):
    app.register_blueprint(api_bp, url_prefix='/api')