import json 
import azure.functions as func
import requests


def main(event):

    logglyendpoint = "<Loggly HTTP Endpoint with tag goes here>"
    package = event.get_body()
    package = json.dumps(package.decode("utf-8"))
    r = requests.post(logglyendpoint, json=package)
    return 

   

