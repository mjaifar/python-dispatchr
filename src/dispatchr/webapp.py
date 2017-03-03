from flask import Flask, jsonify
from flask_restful import Resource, Api
from data.models import ServerService
import json

app = Flask(__name__)
api = Api(app)


class RegistrarResource(Resource):
    def get(self):
        server = ServerService('https', '54.25.14.36', '443')
        return jsonify(server.to_json())


api.add_resource(RegistrarResource, '/registrar')


def main():
    app.run(debug=True)
