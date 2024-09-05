from flask_restful import Resource, reqparse
from app.models import Booking, db

booking_parser = reqparse.RequestParser()
booking_parser.add_argument('property_id', type=int, required=True)
booking_parser.add_argument('user_id', type=int, required=True)
booking_parser.add_argument('start_date', type=str, required=True)
booking_parser.add_argument('end_date', type=str, required=True)
booking_parser.add_argument('status', type=str, required=True)

class BookingResource(Resource):
    def get(self, id):
        booking = Booking.query.get_or_404(id)
        return {
            'id': booking.id,
            'property_id': booking.property_id,
            'user_id': booking.user_id,
            'start_date': booking.start_date.isoformat(),
            'end_date': booking.end_date.isoformat(),
            'status': booking.status
        }

    def put(self, id):
        args = booking_parser.parse_args()
        booking = Booking.query.get_or_404(id)
        booking.property_id = args['property_id']
        booking.user_id = args['user_id']
        booking.start_date = args['start_date']
        booking.end_date = args['end_date']
        booking.status = args['status']
        db.session.commit()
        return {'message': 'Booking updated successfully'}

    def delete(self, id):
        booking = Booking.query.get_or_404(id)
        db.session.delete(booking)
        db.session.commit()
        return {'message': 'Booking deleted successfully'}

class BookingListResource(Resource):
    def get(self):
        bookings = Booking.query.all()
        return [
            {
                'id': b.id,
                'property_id': b.property_id,
                'user_id': b.user_id,
                'start_date': b.start_date.isoformat(),
                'end_date': b.end_date.isoformat(),
                'status': b.status
            } for b in bookings
        ]

    def post(self):
        args = booking_parser.parse_args()
        booking = Booking(
            property_id=args['property_id'],
            user_id=args['user_id'],
            start_date=args['start_date'],
            end_date=args['end_date'],
            status=args['status']
        )
        db.session.add(booking)
        db.session.commit()
        return {'message': 'Booking created successfully'}, 201
