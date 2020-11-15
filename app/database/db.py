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
        return self.tempTransform(temps)

    def getAverage(self):
        after = time.time() - (60 * 60 * 24 * 30)
        temps = self.client.db.temp.find({"timestamp": {"$gt": after}})
        return self.tempTransform(temps)

    def getLatest(self):
        temp = self.client.db.temp.find().sort({'timestamp':-1}).limit(1)
        return self.tempTransform(temp)

    def tempTransform(self, tempData):
        tempTransform = []
        for temp in tempData:
            tempTransform.append({"temp": temp['temp'], "timestamp": temp.get('timestamp', 0)})
        return tempTransform