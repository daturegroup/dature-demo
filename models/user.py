from db import db

# db.String yerine db.varchar kullanılırsa daha iyi olur 

class UserModel(db.Model):
    __tablename__ = "users"

    _id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    # payment_method = db.Column(db.String(80))
    # farm_type = db.Column(db.String(80))
    # location = db.Column(db.String(80))

    sensor_info = db.relationship("SensorInformationModel",lazy = "dynamic") 
    field_info = db.relationship("FieldInformationModel",lazy = "dynamic")


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {
            "user_id" : self._id,
            "username":self.username,
            "password":self.password,
            "field_info" : [field.json() for field in self.field_info.all()],
            "sensor_info": [sensor.json() for sensor in self.sensor_info.all()]
            
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # parametreler **kwargs olarak düzenlenip genelleştirilecek / update_to_db olmalı
    def update_password(self, new_password):
        self.password = new_password
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()

    @classmethod
    def find_by_credentials(cls, username, password):
        return cls.query.filter_by(username = username, password = password).first()


class SensorInformationModel(db.Model):
    __tablename__ = "sensors_info"

    _id = db.Column(db.Integer,primary_key = True)
    sensor_type = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('users._id'))

    # users = db.relationship('UserModel')

    def __init__(self, user_id, sensor_type = "undefined"):
        self.user_id = user_id
        self.sensor_type = sensor_type
  
    def json(self):
        return {
            "user_id":self.user_id,
            "sensor_id":self._id,
            "sensor_type":self.sensor_type
        }         
                  

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def get_device_id(self, jsonify = False):
        if jsonify :
            return {"sensor_unique_id":str(self.user_id) + "0" + str(self._id)}
        else:
            return str(self.user_id) + "0" + str(self._id)


class FieldInformationModel(db.Model):
    __tablename__ = "field_info"

    _id = db.Column(db.Integer,primary_key = True)
    field_name = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('users._id'))

    def __init__(self , user_id , field_name = "undefined" ):
        self.user_id = user_id
        self.field_name = field_name

    def json(self):
        return {
            "user_id" : self.user_id,
            "field_name" : self.field_name
        }
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



