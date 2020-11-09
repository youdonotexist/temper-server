from flask_restful import Api, Resource

api = Api()

def init_api(app):
    api.init_app(app)

