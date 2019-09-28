from flask_restful import Resource, reqparse 
from models.user import UserModel

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
    
class Users(Resource):
    def get(self):
        return {"users" : [user.json() for user in UserModel.query.all()] }