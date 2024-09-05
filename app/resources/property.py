from flask_restful import Resource, reqparse
from app.models import Property, db

property_parser = reqparse.RequestParser()
property_parser.add_argument('name', type=str, required=True)
property_parser.add_argument('location', type=str, required=True)
property_parser.add_argument('price', type=float, required=True)

class PropertyResource(Resource):
    def get(self, id):
        property = Property.query.get_or_404(id)
        return {'id': property.id, 'name': property.name, 'location': property.location, 'price': property.price}

    def put(self, id):
        args = property_parser.parse_args()
        property = Property.query.get_or_404(id)
        property.name = args['name']
        property.location = args['location']
        property.price = args['price']
        db.session.commit()
        return {'message': 'Property updated successfully'}

    def delete(self, id):
        property = Property.query.get_or_404(id)
        db.session.delete(property)
        db.session.commit()
        return {'message': 'Property deleted successfully'}

class PropertyListResource(Resource):
    def get(self):
        properties = Property.query.all()
        return [{'id': p.id, 'name': p.name, 'location': p.location, 'price': p.price} for p in properties]

    def post(self):
        args = property_parser.parse_args()
        property = Property(name=args['name'], location=args['location'], price=args['price'])
        db.session.add(property)
        db.session.commit()
        return {'message': 'Property created successfully'}, 201
