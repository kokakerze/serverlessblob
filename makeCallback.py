import json
import ast
import requests


def lambda_handler(event, context,):
    NewImage = event["Records"][0]['dynamodb']['NewImage']
    if "labels" in NewImage:
        callback = event["Records"][0]['dynamodb']['NewImage']['callback']['S']
        pid = event["Records"][0]['dynamodb']['NewImage']['pid']['S']
        labels = event["Records"][0]['dynamodb']['NewImage']['labels']['S']
        labels_list = ast.literal_eval(labels)
        data_json = {
            "pid": pid,
            "labels": labels_list,
        }
        # data_json = json.dumps(data)
        print(data_json)
        headers = {"content-type": "application/json"}
        requests.post(callback, json=data_json, headers=headers)
        return data_json


