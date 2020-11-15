import os
from flask import Flask, request, jsonify, json
from database.db import Database
from service.api import init_api

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

init_api(app)
database = Database(app)

@app.route('/saveTemp', methods=['POST'])
def saveTemp():
    data = request.get_json(force=True)
    database.saveTemp(data)
    return jsonify({"success": "true"})

@app.route('/getTemp', methods=['GET'])
def getTemps():
    data = database.getTemps()
    return jsonify(data)

@app.route('/average', methods=['GET'])
def getAverage():
    data = database.getAverage()
    return jsonify(data)

@app.route('/latest', methods=['GET'])
def getLatest():
    data = database.getLatest()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')