import decimal
import unittest
from datetime import datetime
from unittest import mock
import boto3

from quokkakit.lambdas.utils.common import DecimalEncoder, getValueOfTimeEndDay, getValueOfTimeStartDay

class TestTimeFunctions(unittest.TestCase):
    def test_getValueOfTimeStartDay(self):
        time = datetime(2024, 3, 27, 10, 30, 0)
        result = getValueOfTimeStartDay(time)
        expected = datetime(2024, 3, 27, 0, 0, 0).timestamp()
        self.assertEqual(result, expected)

    def test_getValueOfTimeEndDay(self):
        time = datetime(2024, 3, 27, 10, 30, 0)
        result = getValueOfTimeEndDay(time)
        expected = datetime(2024, 3, 27, 23, 59, 59).timestamp()
        self.assertEqual(result, expected)

class TestDecimalEncoder(unittest.TestCase):
    def test_decimalEncoder_float(self):
        value = decimal.Decimal('10.123')
        encoder = DecimalEncoder()
        result = encoder.default(value)
        expected = float(value)
        self.assertEqual(result, expected)

    def test_decimalEncoder_int(self):
        value = decimal.Decimal('10.00')
        encoder = DecimalEncoder()
        result = encoder.default(value)
        expected = int(value)
        self.assertEqual(result, expected)


class TestHandler(unittest.TestCase):
    def handler(self):
        dynamodb = boto3.client('dynamodb')
        response = dynamodb.put_item(TableName='NoteTableTest', Item={'id': {'S': '1'}, 'content': {'S': 'Item 1'}, 'timestamp': {'N': 123}})
        return response

    @mock.patch("boto3.client")
    def test_handler(self, mock_client):
        mock_dynamodb = mock_client.return_value
        mock_dynamodb.put_item.return_value = {'ResponseMetadata': {'HTTPStatusCode': 200}}

        response = self.handler()

        mock_client.assert_called_once_with('dynamodb')
        mock_dynamodb.put_item.assert_called_once_with(
            TableName='NoteTableTest',
            Item={'id': {'S': '1'}, 'content': {'S': 'Item 1'}, 'timestamp': {'N': 123}}
        )
        self.assertEqual(response, {'ResponseMetadata': {'HTTPStatusCode': 200}})

if __name__ == '__main__':
    unittest.main()