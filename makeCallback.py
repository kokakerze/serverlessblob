import json
import ast
import requests


def lambda_handler(event, context,):
    NewImage = event["Records"][0]['dynamodb']['NewImage']
    if "labels" in NewImage:
        callback = event["Records"][0]['dynamodb']['NewImage']['callback']['S']
        labels = event["Records"][0]['dynamodb']['NewImage']['labels']['S']
        data = ast.literal_eval(labels)
        data_json = json.dumps(data)
        requests.post(callback, json=data_json)

        return data_json
