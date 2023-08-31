import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    primary_key = str(event.get('pathParameters', {}).get('id'))
    
    response = table.get_item(
        Key={'id': primary_key}
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "data": response.get('Item',{}).get('data'),
        }),
    }
