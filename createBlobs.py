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
    random = randint(3, 11)
    blob_id = shortuuid.ShortUUID().random(length=random)
    key = blob_id + ".jpeg"
    path = s3.generate_presigned_url('put_object', Params={'Bucket': bucket_name, 'Key': key}, ExpiresIn=3600,
                                     HttpMethod='PUT')
    blob = {}
    blob.update({'pid': blob_id, 'path': path, 'key': key})
    table = dynamodb.Table(table_name)
    response = table.put_item(TableName=table_name, Item=blob)
    return {
        "statusCode": 201,
        "headers": {},
        "body": json.dumps(
            {
                "message": "Blob Created",
                "id": blob_id,
                "path": path,

            }
        )
    }
