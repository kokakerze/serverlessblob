import json

import requests


def lambda_handler(event, context,):
    NewImage = event["Records"][0]['dynamodb']['NewImage']
    if "labels" in NewImage:
        callback = event["Records"][0]['dynamodb']['NewImage']['callback']['S']
        labels = event["Records"][0]['dynamodb']['NewImage']['labels']['S']
        data = json.dumps(labels)
        requests.post(callback, json=data)
    return NewImage
