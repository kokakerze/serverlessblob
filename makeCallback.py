import os

import boto3
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context, dynamodb=None):
    pid = event["Records"][0]['dynamodb']['NewImage']['pid']['S']

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table_name = os.environ.get('BLOBS_TABLE')
    table = dynamodb.Table(table_name)
    response = table.query(
        KeyConditionExpression=Key('pid').eq(pid)
    )
    return response['Items']
