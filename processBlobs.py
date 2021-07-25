import os

import boto3

s3 = boto3.client('s3')
client = boto3.client('rekognition')
table_name = os.environ.get('BLOBS_TABLE')
bucket_name = os.environ.get('BLOBS_BUCKET')


def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    pid = file_key.replace(".jpeg", "")
    labels = detect_labels(file_key, bucket_name)
    print("Labels detected: " + str(labels))
    table = boto3.resource('dynamodb').Table(table_name)
    response = table.update_item(Key={"pid": pid},
                                 UpdateExpression='SET labels = :val1 ',
                                 ExpressionAttributeValues={
                                     ':val1': str(labels)
                                 }
                                 )
    return response


def detect_labels(photo, bucket):
    response = client.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
                                    MaxLabels=10)

    print('Detected labels for ' + photo)
    print()
    for label in response['Labels']:
        print("Label: " + label['Name'])
        print("Confidence: " + str(label['Confidence']))
        print("Instances:")
        for instance in label['Instances']:
            print("  Bounding box")
            print("    Top: " + str(instance['BoundingBox']['Top']))

            print("    Left: " + str(instance['BoundingBox']['Left']))
            print("    Width: " + str(instance['BoundingBox']['Width']))
            print("    Height: " + str(instance['BoundingBox']['Height']))
            print("  Confidence: " + str(instance['Confidence']))

        print("Parents:")
        for parent in label['Parents']:
            print("   " + parent['Name'])
        print("----------")
        print()
    return response['Labels']
