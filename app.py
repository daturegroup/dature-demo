from flask import Flask 
from flask_restful import Api ,Resource

from resources.user import UserRegister
from resources.sensor import SensorRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:umut@127.0.0.1:5432/trial_database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'umut'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()
    

class Home(Resource):
    def get(self):
        return "This is test API, Welcome :)"



# http://127.0.0.1:5000 
api.add_resource(Home, '/') 

api.add_resource(UserRegister, "/signin")

api.add_resource(SensorRegister, "/sensor")

# If the debug flag is 'True' set the server 
# will automatically reload for code changes 
# and show a debugger in case an exception happened.
if __name__ == "__main__":
    from db import db, Database
    db.init_app(app)
    Database.initialize()
    app.run(port=5000, debug=True) 



