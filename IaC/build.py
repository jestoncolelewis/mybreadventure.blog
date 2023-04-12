from functions import *
import os

name = "mybreadventure.blog"

# s3 lambda variables
path = os.getcwd()

file = "index.zip"

path = path + "/" + file

key = build_lambda_bucket(name, path, file)

# s3 web variables
web_path = os.path.abspath(os.path.join(path, os.pardir))

files = [] # load all desired files and folders in web_path

with os.scandir('..') as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            if not entry.name.endswith('.md'):
                if not entry.name.endswith('.http'):
                    files.append(entry.name)
        if not entry.name.startswith('.') and entry.is_dir():
            if not entry.name.startswith('IaC'):
                files.append(entry.name)

build_web_bucket(name, web_path, files)

# dynamo variables
keys = [{"AttributeName": "post-num", "KeyType": "HASH"}]

attributes = [{"AttributeName": "post-num", "AttributeType": "N"}]

build_dynamo(name, keys, attributes)

# lambda variables
lang = "python3.9"

iam = build_iam(name)

code = [name, key]

description = "function for retrieving and updating page views"

build_lambda(name, lang, iam, code, description)