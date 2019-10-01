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

        if FieldInformationModel.find_by_user_id_and_field_name(current_user._id , data["field_name"]):
            return {"message": "Error ! You already have a field same with this field name"}
        
        new_field = FieldInformationModel(current_user._id , data["field_name"])
        new_field.save_to_db()
        return {"message" : "Created successfully."} , 201
        
    
    def delete(self):
        data = FieldInformation.parser.parse_args()
        if not UserModel.find_by_credentials(data["username"],data["password"]):
            return {"message": "Wrong username or password"}, 400

        current_user = UserModel.find_by_credentials(data["username"],data["password"])

        if not FieldInformationModel.find_by_user_id_and_field_name(current_user._id , data["field_name"]):
            return {"message": "Field that you want to delete is not found"}

        current_field =  FieldInformationModel.find_by_user_id_and_field_name(current_user._id , data["field_name"])
        current_field.delete_field_from_db()
        return current_field.json() , {"message" : "Field Deleted Successfully."}


    
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
    parser.add_argument("field_name",
        type = str,
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

        current_user = UserModel.find_by_credentials(data["username"], data["password"])

        if not FieldInformationModel.find_by_user_id_and_field_name(current_user._id , data["field_name"]):
            return {"message": "Field name is not found."}, 400

        if SensorInformationModel.find_by_field_name_and_sensor_type(data["field_name"] , data["sensor_type"]):
            return {"message": "This sensor_type is used for this field. Try different!"}


        new_sensor = SensorInformationModel(current_user._id , data["field_name"] , data["sensor_type"])
        new_sensor.save_to_db()
        return new_sensor.get_device_id(jsonify = True)

    
    def put(self):
        data = SensorInformation.parser.parse_args()
        if not UserModel.find_by_credentials(data["username"],data["password"]):
            return {"message": "Wrong username or password"}, 400

        current_user = UserModel.find_by_credentials(data["username"],data["password"])
        if not FieldInformationModel.find_by_user_id_and_field_name(current_user._id , data["field_name"]):
            return {"message": "Field name is not found."}, 400

        if not SensorInformationModel.find_by_user_id_and_sensor_type(current_user._id , data["sensor_type"]):
            return {"message": "Sensor type is not found."}, 400

        new_field = SensorInformationModel.find_by_user_id_and_sensor_type(current_user._id , data["sensor_type"])
        new_field.update_field(data["field_name"])
        return new_field.json()
        


        
        



