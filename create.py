import json
import os
import time
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')

def create(event, context):
    data = json.loads(event['body'])

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    patient = {
        'id': str(uuid.uuid1()),
        'name': data['name'],
        'birthdate': data['birthdate'],
        'city': data['city'],
        'zipCode': data['zipCode'],
        'street': data['street'],
        'phone': data['phone'],
        'checks': data['checks'],
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp
    }

    table.put_item(Item=patient)

    response = {
        "statusCode": 200,
        "body": json.dumps(patient),
        "headers": {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": "true"
        }
    }

    return response