import boto3

dynamo = boto3.client('dynamodb')
dynamor = boto3.resource('dynamodb')
table = dynamor.Table('breadtest') # type: ignore

# request a sum of items and count backwards from the the total for the most recent item
def lambda_handler(event, context):
    posts = table.item_count('breadtest')
    print(posts)

    response = dynamo.get_item(
        Key = {'post_num':{'N':'0'}},
        TableName = 'breadtest'
    )

    return response