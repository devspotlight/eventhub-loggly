import json 
import azure.functions as func
import logging
import requests


def main(event):
    test = event.get_body()
    test2 = test.decode("utf-8")
    test3 = json.dumps(test2)
    r = requests.post('http://logs-01.loggly.com/inputs/ff2337d9-dd24-4030-8c6e-309ae53738db/tag/http/', data = test3)
    return 

   
