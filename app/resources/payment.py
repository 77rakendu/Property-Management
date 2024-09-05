from flask_restful import Resource, reqparse
from app.models import Payment, db

payment_parser = reqparse.RequestParser()
payment_parser.add_argument('booking_id', type=int, required=True)
payment_parser.add_argument('amount', type=float, required=True)
payment_parser.add_argument('status', type=str, required=True)

class PaymentResource(Resource):
    def get(self, id):
        payment = Payment.query.get_or_404(id)
        return {
            'id': payment.id,
            'booking_id': payment.booking_id,
            'amount': payment.amount,
            'status': payment.status
        }

    def put(self, id):
        args = payment_parser.parse_args()
        payment = Payment.query.get_or_404(id)
        payment.booking_id = args['booking_id']
        payment.amount = args['amount']
        payment.status = args['status']
        db.session.commit()
        return {'message': 'Payment updated successfully'}

    def delete(self, id):
        payment = Payment.query.get_or_404(id)
        db.session.delete(payment)
        db.session.commit()
        return {'message': 'Payment deleted successfully'}

class PaymentListResource(Resource):
    def get(self):
        payments = Payment.query.all()
        return [
            {
                'id': p.id,
                'booking_id': p.booking_id,
                'amount': p.amount,
                'status': p.status
            } for p in payments
        ]

    def post(self):
        args = payment_parser.parse_args()
        payment = Payment(
            booking_id=args['booking_id'],
            amount=args['amount'],
            status=args['status']
        )
        db.session.add(payment)
        db.session.commit()
        return {'message': 'Payment created successfully'}, 201
