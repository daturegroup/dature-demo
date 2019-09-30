import requests
import json


def post(num = 0):
    header = {"Content-Type":"application/json"}

    #data = json.dumps({"username": "cankara" , "password" : "1234"})
    #server_url = "http://127.0.0.1:5000/user"
    
    #data = json.dumps({"username": "cankara" , "password" : "1234" , "sensor_type" : "nem"})
    #server_url = "http://127.0.0.1:5000/user/sensor"

    data = json.dumps({"username": "cankara" , "password" : "1234" , "field_name" : "Marul"})
    server_url = "http://127.0.0.1:5000/user/field"

      
    try:    
        res = requests.post(url = server_url,headers = header,data = data)
        return res.status_code, res.content 
    except:
        return 400

print(post())

