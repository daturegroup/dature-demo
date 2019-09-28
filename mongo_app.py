from models.sensor import Sensor
from database import Database

sensor1 = Sensor(1 ,20 ,34)

Database.initialize()

sensor1.save_to_mongo()

