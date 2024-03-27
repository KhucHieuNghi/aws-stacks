from __future__ import print_function
import json
import os
import boto3
from utils.common import *

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# set environment variable
TABLE_NAME = os.environ['NoteItemsTable']

def lambda_handler(event = {}, context = {}):

    payload = dict(event)

    body = payload.get('body', dict())

    query = payload.get('query', dict());

    method = payload.get('method', 'GET');

    table = dynamodb.Table(TABLE_NAME)

    username = query.get('username', None)

    if method == 'GET':
        page = query.get('page', 1)

        data = []

        if  username == None: data = scanAllPagination(page, table)
        else: data = queryPaginationByUsername(page, username, table)

        return {
            'statusCode': 200,
            "data": data
        }

    if body == None: raise Exception("Body empty");

    if  body.get('content', None) == None or body.get('username', None) == None:
            raise Exception("Method POST, Body missing fields")

    if method == 'POST':
        item = putNoteItem(body, table)

        return {
            'statusCode': 200,
            'data': json.dumps(item, indent=4, cls=DecimalEncoder)
        }
    
    raise Exception("Nothing")