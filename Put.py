import json
import boto3
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    # TODO implement
    table = dynamodb.Table('APILambdaTable')
    
    response = table.put_item(
        Item=event
    )
    return {
        'code': 200,
        'message': "Successfully Inserted one item in the Table"
    }
