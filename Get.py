import json    
import boto3

dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):

    table = dynamodb.Table('APILambdaTable')
    
    response = table.get_item(Key=event)
    try:
        return response['Item']
    except KeyError:
        return{
            'statusCode': '404',
            'Message': 'Not found'
        }
