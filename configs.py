import configparser

config = configparser.ConfigParser()
config.read("uwsgi.ini")

mongo_port =  config["mongodb"]["port"]

mongo_host = config["mongodb"]["host"]

mongo_URI =  "mongodb://" +  mongo_host + ":" + mongo_port

print(mongo_URI)