import boto3

dynamo = boto3.client('dynamodb')
dynamor = boto3.resource('dynamodb')
table = dynamor.Table('breadtest') # type: ignore

def lambda_handler():
    response = []
    posts = 3 # table.item_count

    for i in range(posts):
        item = dynamo.get_item(
            Key = {'post_num':{'N':'{}'.format(i)}},
            TableName = 'breadtest'
        )
        response.append(str(item))

    return response