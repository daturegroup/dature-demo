from db import Database
import datetime

class SensorModel(object):
    def __init__(self, _id, moisture, temperature, date=datetime.datetime.now()):
        self._id = _id
        self.date = date
        self.moisture = moisture
        self.temperature = temperature       
    
    @staticmethod
    def get_all():
        return [result for result in Database.find("sensor_trial",{})]

    def save_to_mongo(self):
        Database.insert("sensor_trial",self.json())

    def json(self):
        return {
            "id": self._id,
            "date": self.date,
            "temperature": self.temperature,
            "moisture" : self.moisture
        }