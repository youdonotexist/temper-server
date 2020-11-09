from flask_pymongo import PyMongo
import time

class Database(): 
    client = None
    def __init__(self, app):
        print("init db: " + app.config["MONGO_URI"])
        self.client = PyMongo(app)

    def saveTemp(self, temp):
        temp['timestamp'] = temp.get('timestamp', time.time())
        self.client.db.temp.insert_one(temp)

    def getTemps(self):
        temps = list(self.client.db.temp.find({}))
        tempTransform = []
        for temp in temps:
            tempTransform.append({"temp": temp['temp'], "timestamp": temp.get('timestamp', 0)})

        return tempTransform
