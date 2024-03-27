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

    payloadstr = dict(event).get('body', dict())
    
    payload = json.loads(payloadstr)
    
    body = payload.get('body', dict())

    query = payload.get('query', dict());

    method = payload.get('method', 'GET');

    table = dynamodb.Table(TABLE_NAME)

    username = query.get('username', None)

    if method == 'GET':
        page = query.get('page', 1)

        data = []

        if bool(username): data = queryPaginationByUsername(page, username, table)
        else: data = scanAllPagination(page, table)
        
        return {"data": data, "httpCode": 200}

    if body == None: raise Exception("Body empty");

    if  not bool(body.get('content', None)) or not bool(body.get('username', None)):
            raise Exception("Method POST, Body missing fields")

    if method == 'POST':
        item = putNoteItem(body, table)
        
        return {"httpCode": 200, "data": item}
    
    raise Exception("Nothing")