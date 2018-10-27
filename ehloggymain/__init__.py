import json 
import azure.functions as func
import requests


def main(event):
    package = event.get_body()
    package = json.dumps(package.decode("utf-8"))
    r = requests.post('http://logs-01.loggly.com/inputs/ff2337d9-dd24-4030-8c6e-309ae53738db/tag/ehlog/', data = package)
    return 

   
