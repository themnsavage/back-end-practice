import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    print(event)
    body = json.loads(event["body"])
    item = {
        'id': body['id'],
        'data': body['data']
    }

    response = table.put_item(Item=item)
    print('made pass put item')
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Item was added",
        }),
    }
