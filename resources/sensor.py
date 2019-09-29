from flask import jsonify
from flask_restful import Resource, reqparse
from models.sensor import SensorModel
from db import Database


class SensorRegister(Resource):
    
    parser = reqparse.RequestParser()
    
    parser.add_argument("sensor_id",
        type = int,
        required = True,
        help = "This field can not be left blank"
    )
    parser.add_argument("moisture",
        type = int,
        required = True,
        help = "This field can not be left blank"
    )
    
    parser.add_argument("temperature",
        type =int,
        required = True,
        help = "This field can not be left blank"
    )   
    
    def get(self):
        return jsonify({"Sensor Values": SensorModel.get_all()})
    
    
    def post(self):
        data = SensorRegister.parser.parse_args()

        sensor_data = SensorModel(data["sensor_id"],data["moisture"],data["temperature"])
        try:
            sensor_data.save_to_mongo()
        except:
            return {"message":"Database fucked up"} , 400

        return sensor_data.jsonify()

class Sensors(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("moisture",
        type = int,
        required = True,
        help = "This field can not be left blank"
    )
    parser.add_argument("temperature",
        type =int,
        required = True,
        help = "This field can not be left blank"
    )

    def post(self, sensor_id):
        data = Sensors.parser.parse_args()

        sensor_data = SensorModel(sensor_id, data["moisture"], data["temperature"])

        try:
            sensor_data.save_to_mongo()
        except:
            return {"message":"Database fucked up"} , 400

        return sensor_data.jsonify()

    def get(self,sensor_id):
        if SensorModel.find_by_id(sensor_id):
            return jsonify({"data":SensorModel.find_by_id(sensor_id)})
        else:
            return {"message":"data by sensor by id : {} is not found".format(sensor_id)}

    # Konuşulcak    
    def put(self):
        pass

    # Konuşulcak
    def delete(self):
        pass 

