from flask import Flask
from flask_restful import Api ,Resource

from resources.user import UserRegister, Users ,SensorInformation , FieldInformation
from resources.sensor import SensorRegister, Sensors 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:1234@127.0.0.1:5432/trial_database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b')\xe4\xe7]\xdcIYF>*\x8a\xb7\x91[\xda6'  #secret-key generetad by os.urandom()
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()
    

class Home(Resource):
    def get(self):
        return "This is test API, Welcome :)"
 


# http://127.0.0.1:5000 
api.add_resource(Home, '/') 
# Post and add postgres to user and password
api.add_resource(UserRegister, "/user")
# Post and add postgres to sensor information  
api.add_resource(SensorInformation, "/user/sensor")  
#Post and add postrgres to field information
api.add_resource(FieldInformation, "/user/field")
# Postgre list all users /get
api.add_resource(Users,"/users")
# Mongodb insert sensor values / post
# Mongodb List all collection values /get
api.add_resource(SensorRegister, "/sensors")                      
# For collect wemos data from specific id /post
# return specific id's sensor datas /get
api.add_resource(Sensors, "/sensor/<int:sensor_id>")




# If the debug flag is 'True' set the server 
# will automatically reload for code changes 
# and show a debugger in case an exception happened.
if __name__ == "__main__":
    from db import db, Database
    db.init_app(app)
    Database.initialize()
    app.run(port=5000, debug=True)
    






