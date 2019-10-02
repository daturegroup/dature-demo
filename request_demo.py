import requests
import json


def post(num = 0):
    header = {"Content-Type":"application/json"}

    #data = json.dumps({"username": "egemen" , "password" : "1234"})
    #server_url = "http://127.0.0.1:5000/user"

    #data = json.dumps({"username": "egemen" , "password" : "1234" , "field_name" : "Armut"})
    #server_url = "http://127.0.0.1:5000/user/field"

    # data = json.dumps({"username": "can" , "password" : "1234" , "field_name" : "Marul" , "sensor_type" : "nem2"})
    # server_url = "http://127.0.0.1:5000/user/sensor"

    data = json.dumps({"moisture": 15.3, "temperature" : 20.2 })
    server_url = "http://127.0.0.1:5000/sensor/1-4"
      
    try:    
        res = requests.post(url = server_url,headers = header,data = data)   #request.post || request.put || request.delete
        return res.status_code, res.content 
    except:
        return 400

print(post())




