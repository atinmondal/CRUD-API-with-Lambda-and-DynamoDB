import boto3

dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    table = dynamodb.Table('APILambdaTable')
    
    response = table.update_item(
        Key={
            'Student_Id': event['id']
        },
        UpdateExpression='SET #name = :val1',
        ExpressionAttributeValues={
        ":val1": event['newName']
        },
        ExpressionAttributeNames={
        "#name": event['attributeName']
        },
        ConditionExpression='attribute_not_exists(deletedAt)', # Do not update if deleted
        ReturnValues="UPDATED_NEW"
    )
    return {
        'code': 200,
        'message': f"Successfully updated attributevalue {response['Attributes']}"
    }
    
