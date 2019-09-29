import requests
import json


def post(num = 0):
    header = {"Content-Type":"application/json"}
    # data = json.dumps({"username": "egemen" , "password" : "egemen123"}) /users
    # data = json.dumps({"sensor_id": 4 , "moisture" : 5,"temperature":40}) /sensor
    # data = json.dumps({"moisture" : 5,"temperature":40}) /sensor/<sensor_id>
    data = json.dumps({"username": "nailcan" , "password" : "1234"})
    server_url = "http://127.0.0.1:5000/user/sensor"
    try:    
        res = requests.post(url = server_url,headers = header,data = data)
        return res.status_code, res.content 
    except:
        return 400

print(post())