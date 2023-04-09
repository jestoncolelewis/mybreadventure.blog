import boto3

dynamo = boto3.client('dynamodb')

# request a sum of items and count backwards from the the total for the most recent item