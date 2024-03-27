from __future__ import print_function
import json
import uuid
import decimal
from datetime import datetime
from boto3.dynamodb.conditions import Key

pagesize = 5

def getValueOfTimeStartDay(time: datetime):
    return time.replace(hour=0, minute=0, second=0, microsecond=0).timestamp()

def getValueOfTimeEndDay(time: datetime):
    return time.replace(hour=23, minute=59, second=59, microsecond=0).timestamp()


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def scanAllPagination(page = 1, table:any = None):

    remain_page = page
    result = [];

    scan_kwargs = {
        "IndexName": 'src_idx',
        "Limit": pagesize,
        "KeyConditionExpression": Key('src').eq('QUOKKA'),
        "ScanIndexForward": False,
    }

    try:
        done = False
        start_key = None
        while not done:
            if start_key:
                scan_kwargs["ExclusiveStartKey"] = start_key

            response = table.query(**scan_kwargs)
            start_key = response.get("LastEvaluatedKey", None)
            done = start_key is None
            
            if remain_page == 1: 
                done = True
                result.extend(response.get("Items", []))

            remain_page -= 1;

    except Exception as err:
        print(err)
        raise Exception("Batch error")

    return result


def queryPaginationByUsername(page = 1, username: str = '' ,table:any = None):

    remain_page = page
    result = [];
    scan_kwargs = {
        "IndexName": 'username_idx',
        "Limit": pagesize,
        "KeyConditionExpression": Key('username').eq(username),
        "ScanIndexForward": False,
    }

        
    try:
        done = False
        start_key = None
        while not done:
            if start_key:
                scan_kwargs["ExclusiveStartKey"] = start_key

            response = table.query(**scan_kwargs)
            start_key = response.get("LastEvaluatedKey", None)
            done = start_key is None
            
            if remain_page == 1: 
                done = True
                result.extend(response.get("Items", []))

            remain_page -= 1;

    except Exception as err:
        print(err)
        raise Exception("Batch error")

    return result

def putNoteItem(item:any, table:any):
    payload = {
                'id': str(uuid.uuid4()),
                'content': item.get('content', '---'),
                'timestamp': int(datetime.utcnow().timestamp()),
                'username': item.get('username', 'empty'),
                'src': 'QUOKKA'
            }
    table.put_item(Item=payload);
    return payload;
        