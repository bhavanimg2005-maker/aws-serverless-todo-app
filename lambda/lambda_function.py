import json
import boto3
import uuid

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def lambda_handler(event, context):

    method = event['httpMethod']

    # GET request - Fetch all tasks
    if method == 'GET':

        response = table.scan()

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(response['Items'])
        }

    # POST request - Add a new task
    elif method == 'POST':

        body = json.loads(event['body'])

        item = {
            'id': str(uuid.uuid4()),
            'task': body['task']
        }

        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Task Added'})
        }

    # Unsupported HTTP method
    return {
        'statusCode': 400,
        'body': json.dumps({'message': 'Invalid HTTP Method'})
    }
