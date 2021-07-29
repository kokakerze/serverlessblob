import os

import boto3
import simplejson as json
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ.get('BLOBS_TABLE')
    table = dynamodb.Table(table_name)
    order_id = event['pathParameters']['id']
    response = table.query(KeyConditionExpression=Key('pid').eq(order_id))

    return {
        "statusCode": 200,
        "headers": {"content-type": "application/json"},
        "body": json.dumps(response['Items'])
    }
