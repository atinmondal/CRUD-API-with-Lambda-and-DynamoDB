import json
import boto3
def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('APILambdaTable')
    
    response = table.delete_item(Key={
        'Student_Id': event['id']
    })
    return {
        'statusCode': 200,
        'message': f"Successfully deleted the item no: {event['id']}"
    }
