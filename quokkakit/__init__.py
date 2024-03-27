# from __future__ import print_function
# import json
# import uuid
# import decimal
# import os
# import boto3
# from datetime import datetime
# from boto3.dynamodb.conditions import Key, Attr
# from botocore.exceptions import ClientError

# from utils.common import *


# # Get the service resource.
# dynamodb = boto3.resource('dynamodb')

# # set environment variable
# TABLE_NAME = os.environ['Quokka4Table']

# def lambda_handler(event, context):

#     payload = dict(event)

#     body = payload.get('body', None)

#     query = payload.get('query', dict());

#     method = payload.get('method', 'GET');

#     table = dynamodb.Table(TABLE_NAME)

#     result=[]

#     key_condition_expression = None

#     username = query.get('username', None)

#     if username:
#         key_condition_expression = Key('username').eq(username)

#     # current_time = query.get('current_time', None)
#     # if current_time:
        
#     #     if len(str(current_time)) == 13: current_time = int(current_time)/1000 
#     #     else: current_time = int(current_time);

#     #     start_timestamp = getValueOfTimeStartDay(datetime.fromtimestamp(current_time))
#     #     end_timestamp = getValueOfTimeEndDay(datetime.fromtimestamp(current_time))

#     #     key_condition_expression = Key('timestamp').between(start_timestamp, end_timestamp)

#     #     if key_condition_expression:
#     #         key_condition_expression += ' AND '


    
#     if method == 'GET':
#         # pagesize = 5
#         page = query.get('page', 1)
#         # remain_page = page

#         if  username == None:

#             result = scanAllPagination(page, table)
#             # scan_kwargs = {
#             #     "IndexName": 'timestamp_idx',
#             #     "Limit": pagesize,
#             #     "ScanIndexForward": False,
#             # }

            
#             # try:
#             #     done = False
#             #     start_key = None
#             #     while not done:
#             #         if start_key:
#             #             scan_kwargs["ExclusiveStartKey"] = start_key

#             #         response = table.scan(**scan_kwargs)
#             #         start_key = response.get("LastEvaluatedKey", None)
#             #         done = start_key is None
                    
#             #         if remain_page == 1: 
#             #             done = True
#             #             result.extend(response.get("Items", []))

#             #         remain_page -= 1;

#             # except Exception as err:
#             #     print(err)
#             #     raise Exception("Batch error")

#             return {
#                 'statusCode': 200,
#                 "data": result
#             }
        

#         # by username
        
#         # scan_kwargs = {
#         #     "IndexName": 'username_idx',
#         #     "Limit": pagesize,
#         #     "KeyConditionExpression": key_condition_expression,
#         #     "ScanIndexForward": False,
#         # }

        
#         # try:
#         #     done = False
#         #     start_key = None
#         #     while not done:
#         #         if start_key:
#         #             scan_kwargs["ExclusiveStartKey"] = start_key

#         #         response = table.query(**scan_kwargs)
#         #         start_key = response.get("LastEvaluatedKey", None)
#         #         done = start_key is None
                
#         #         if remain_page == 1: 
#         #             done = True
#         #             result.extend(response.get("Items", []))

#         #         remain_page -= 1;

#         # except Exception as err:
#         #     print(err)
#         #     raise Exception("Batch error")

#         return {
#             'statusCode': 200,
#             "data": queryPaginationByUsername(page, username, table)
#         }

#     if method == 'POST' and not body == None:

#         if  body.get('content', None) == None or body.get('username', None) == None:
#             raise Exception("Method POST, Body missing fields")

#         item = table.put_item(
#             Item={
#                 'id': str(uuid.uuid4()),
#                 'content': body.get('content', '---'),
#                 'timestamp': int(datetime.utcnow().timestamp()),
#                 'username': body.get('username', 'empty')
#             }
#         )

#         return {
#             'statusCode': 200,
#             'data': json.dumps(item, indent=4, cls=DecimalEncoder)
#         }
    
#     raise Exception("Nothing")

# # awslocal lambda invoke --function-name quokkaLambda \
# #     --payload '{"method":"POST","body":{"content":"content nk12","username":"nk2"}}' /Users/nghi.khuc/Documents/pros/notes/quokka-remote/quokkakit/output.txt

# # awslocal lambda invoke --function-name quokkaLambda \
# #     --payload '{"method":"GET","query":{"page":1,"username":"nk"}}' /Users/nghi.khuc/Documents/pros/notes/quokka-remote/quokkakit/output.json