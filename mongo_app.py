from models.sensor import SensorModel
from database import Database


Database.initialize()
sensor1 = SensorModel(101 ,100 ,100)
sensor1.save_to_mongo()

for i in Database.find("sensor_trial",{"id" : 101}):
    print(i)


