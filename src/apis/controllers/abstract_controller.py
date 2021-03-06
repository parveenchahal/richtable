from flask_restful import Resource, reqparse, request, output_json
from flask import jsonify


class Controller(Resource):
    def __init__(self, operations):
        self.operations = operations

    def get(self):
        args = request.args
        id = args.get('id')
        items = self.operations.get(id)
        items = ([item.to_dict() for item in items])
        return output_json(items, 200, {'Content-Type': 'application/json'})

    def post(self):
        json_data = request.get_json(force=True)
        result = self.operations.insert(json_data)
        return result, 201

    def put(self):
        json_data = request.get_json(force=True)
        result = self.operations.update(json_data)
        return result, 200

    def delete(self):
        args = request.args
        id = args['id']
        self.operations.delete(id)
        return "", 200
