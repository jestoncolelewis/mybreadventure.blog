import boto3
import botocore.exceptions

s3 = boto3.client('s3')
s3r = boto3.resource('s3')
lamb = boto3.client('lambda')
iam = boto3.client('iam')
api = boto3.client('apigatewayv2')
dynamo = boto3.client('dynamo')

# build s3 for lambda
def build_lambda_bucket(name, path, file):
    try:
        s3.create_bucket(
            Bucket = name,
            CreateBucketConfiguration = {
                'LocationConstraint': 'us-west-2'
            }
        )
        s3r.meta.client.upload_file(path, name, file) # type: ignore
    except botocore.exceptions.ClientError as err:
        print('{}'.format(err.response['Error']['Message']))
    response = s3.list_objects(Bucket = name)
    objects = list(response.items())
    file = objects[3][1][0].get('Key')
    return file

# build s3 for website
def build_web_bucket(name, path, file):
    try:
        s3.create_bucket(
            Bucket = name,
            CreateBucketConfiguration = {
                'LocationConstraint': 'us-west-2'
            }
        )
        s3r.meta.client.upload_file(path, name, file) # type: ignore
    except botocore.exceptions.ClientError as err:
        print('{}'.format(err.response['Error']['Message']))

# iam creator
def build_iam(name):
    try:
        response = iam.create_role(
            RoleName = name + '-role',
            AssumeRolePolicyDocument = ...,
            Path = '/'
        )
    except botocore.exceptions.ClientError as err:
        print('{}'.format(err.response['Error']['Message']))
    return response.get('Arn')

# build lambda
def build_lambda(name, lang, role, code, desc):
    try:
        response = lamb.create_function(
            Runtime = lang,
            Role = role,
            Code = {
                'S3Bucket': code[0],
                'S3Key': code[1]
            },
            Description = desc,
            FunctionName = name + '-function',
            Handler = 'index.lambda_handler'
        )
        return response.get('FunctionArn')
    except botocore.exceptions.ClientError as err:
        print('{}'.format(err.response['Error']['Message']))
        response = lamb.get_function(FunctionName = name)
        return response['Configuration']['FunctionArn']

# build api
def build_api(name, target):
    try:
        api.create_api(
            Name = name + '-api',
            ProtocolType = 'HTTP',
            CorsConfiguration = {
                'AllowOrigins': ['*']
            },
            Target = target
        )
    except botocore.exceptions.ClientError as err:
        print('{}'.format(err.response['Error']['Message']))

# build dynamo
def build_dynamo(name, keys, attdef):
    try:
        dynamo.create_table(
            TableName = name + '-table',
            KeySchema = keys,
            AttributeDefinitions = attdef,
            ProvisionedThroughput = {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
    except botocore.exceptions.ClientError as err:
        print('{}'.format(err.response['Error']['Message']))