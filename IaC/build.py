from functions import *
import os

name = "mybreadventure.blog"

# s3 lambda variables
path = os.getcwd()

file = "index.zip"

path = path + "/" + file

key = build_lambda_bucket(name, path, file)

# s3 web variables


build_web_bucket(name, path, file)

# dynamo variables
keys = [{"AttributeName": "primary-key", "KeyType": "HASH"}]

attributes = [{"AttributeName": "primary-key", "AttributeType": "N"}]

# lambda variables
lang = "python3.9"

iam = build_iam(name)

code = [name, key]

description = "function for retrieving and updating page views"