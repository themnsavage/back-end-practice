import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    body = json.loads(event["body"])
    primary_key = str(event.get('pathParameters', {}).get('id'))
    
    attribute_name = body["attribute_name"]
    update_value = body["update_value"]
    
    response = table.update_item(
        Key={
            "id": primary_key
        },
        UpdateExpression=f"set #dataAttr=:a",
        ExpressionAttributeNames={
            '#dataAttr': attribute_name
        },
        ExpressionAttributeValues={
            ':a': update_value
        }
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"{attribute_name} value updated to {update_value}",
        }),
    }
