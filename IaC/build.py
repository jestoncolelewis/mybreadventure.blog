from functions import *
import os

name = "mybreadventure.blog"

# s3 lambda variables
path = os.getcwd()

file = "index.zip"

path = path + "/" + file

key = build_lambda_bucket(name, path, file)

# s3 web variables
tree = os.walk('..')
to_upload = {}

for path in tree:
    with os.scandir(path[0]) as it:
        files = []
        for entry in it:
            if not entry.name.startswith('.') and not entry.name.endswith('.md') and not entry.name.endswith('.http') and not entry.name.endswith('.py') and not entry.name.endswith('ipynb') and not path[0].startswith('../.') and entry.is_file():
                files.append(entry.name)
        if not path[0].startswith('../.') and not path[0].startswith('../IaC') and len(files) != 0:
            to_upload[path[0]] = files

build_web_bucket(name, to_upload)

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