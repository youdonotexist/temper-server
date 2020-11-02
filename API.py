from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_pymongo import PyMongo

app = Flask(__name__)
api = Api(app)
mongo = PyMongo(app, config_prefix='MONGO')
APP_URL = "http://127.0.0.1:5000"
app.config["MONGO_DBNAME"] = "students_db"


@app.route('/saveTemp', methods=['PUT'])
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
