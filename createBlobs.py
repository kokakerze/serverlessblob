import json
import os
from random import randint

import boto3
import shortuuid

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('BLOBS_TABLE')
bucket_name = os.environ.get('BLOBS_BUCKET')


def lambda_handler(event, context):
    url = create_callback_url()
    random = randint(3, 11)
    blob_id = shortuuid.ShortUUID().random(length=random)
    key = blob_id + ".jpeg"
    path = s3.generate_presigned_url('put_object', Params={'Bucket': bucket_name, 'Key': key}, ExpiresIn=3600,
                                     HttpMethod='PUT')
    blob = {}
    blob.update({'pid': blob_id, 'key': key, "callback": url})
    table = dynamodb.Table(table_name)
    response = table.put_item(TableName=table_name, Item=blob)
    return {
        "statusCode": 201,
        "headers": {},
        "body": json.dumps(
            {
                "message": "Blob Created",
                "id": blob_id,
                "presigned_url": path,
                "callback_url": url,

            }
        )
    }


def create_callback_url():
    import requests

    r = requests.post('https://webhook.site/token')

    url = 'https://webhook.site/' + r.json()['uuid']
    return url
