# import logging
import json 
import azure.functions as func
# import os
# import sys
import logging
import requests
# import time
# import uuid

def main(event):
    test = event.get_body()
    test2 = test.decode("utf-8")
    test3 = json.dumps(test2)
    r = requests.post('http://logs-01.loggly.com/inputs/ff2337d9-dd24-4030-8c6e-309ae53738db/tag/http/', data = test3)
    # print(json.dumps(test2))
    return 

   




#     logging.info('Python EventHub trigger processed an event: %s',event.get_body().decode('utf-8'))
#     receivedBody = json.loads(open(os.environ['myEventHubMessage']).read())
#     print('Received body:', receivedBody)

# logger = logging.getLogger("azure")



