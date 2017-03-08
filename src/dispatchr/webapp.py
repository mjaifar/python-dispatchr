from flask import Flask, jsonify
from flask_restful import Resource, Api
from dispatchr.dispatchr_controller import DispatchrController
import logging

app = Flask(__name__)
api = Api(app)

controller = DispatchrController()


class RegistrarResource(Resource):
    def __init__(self):
        logging.info('' + controller.tenants_dict.get('1').servers[0].to_string())

    def get(self, tenant_id):
        server = controller.dispatch(tenant_id)
        return jsonify(server.to_json())


api.add_resource(RegistrarResource, '/<string:tenant_id>')


def config_logging():
    logging.basicConfig(filename='dispatchr-logging.log', level=logging.INFO)


def main():
    config_logging()
    app.run(debug=True)
