from flask_restful import Resource, reqparse 
from models.user import UserModel, SensorInformationModel , FieldInformationModel

class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument("username",
        type = str,
        required = True,
        help = "This field can not be left blank"
    )
    parser.add_argument("password",
        type =str,
        required = True,
        help = "This field can not be left blank"
    )

    def post(self):

        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": "A user with that username is already exist"}, 400

        user = UserModel(**data) # (data["username"],data["password"]) 
        user.save_to_db()

        return {"message": "User created succesfully"} , 201

    def put(self):
        data = UserRegister.parser.parse_args()

        if not UserModel.find_by_username(data["username"]):
            return {"message": "A user with that username is not exist"}, 400

        user = UserModel.find_by_username(data["username"])
        user.update_password(data["password"])

        return user.json()

    def delete(self):
        data = UserRegister.parser.parse_args()

        if not UserModel.find_by_username(data["username"]):
            return {"message": "A user with that username is not exist"}, 400
        
        try:
            user = UserModel.find_by_username(data["username"])
            user.delete_from_db()
            return {"message" : "User is deleted succesfully."}
        except:
            return {"message" : "Some errors occured"}



class Users(Resource):
    def get(self):
        return {"users" : [user.json() for user in UserModel.query.all()]}
    
class SensorInformation(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username",
        type = str,
        required = True,
        help = "This field can not be left blank"
    )
    parser.add_argument("password",
        type =str,
        required = True,
        help = "This field can not be left blank"
    )
    parser.add_argument("sensor_type",
        type = str,
        required = True,
        help = "This field can not be left blank"
    )
    

    def post(self):
        data = SensorInformation.parser.parse_args()
        if not UserModel.find_by_credentials(data["username"],data["password"]):
            return {"message": "Wrong username or password"}, 400

        current_user = UserModel.find_by_credentials(data["username"],data["password"])

        new_sensor = SensorInformationModel(user_id = current_user._id , sensor_type = data["sensor_type"])
        new_sensor.save_to_db()
        return new_sensor.get_device_id(jsonify = True)


class FieldInformation(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username",
        type = str,
        required = True,
        help = "This field can not be left blank"
    )
    parser.add_argument("password",
        type =str,
        required = True,
        help = "This field can not be left blank"
    )
    parser.add_argument("field_name",
        type = str,
        required = True,
        help = "This field can not be left blank"
    )
    

    def post(self):
        data = FieldInformation.parser.parse_args()
        if not UserModel.find_by_credentials(data["username"],data["password"]):
            return {"message": "Wrong username or password"}, 400

        current_user = UserModel.find_by_credentials(data["username"],data["password"])

        new_sensor = FieldInformationModel(user_id = current_user._id , field_name = data["field_name"])
        new_sensor.save_to_db()
        return {"message" : "Created successfully."} , 201