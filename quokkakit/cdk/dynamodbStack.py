from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb
)
from constructs import Construct

class DynamodbStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # username, timestamp
        self.dynamodb = dynamodb.TableV2(self, "NoteTable",
            partition_key=dynamodb.Attribute(name="pk", type=dynamodb.AttributeType.STRING),
            table_name='NoteTable',
            # global_secondary_indexes=[dynamodb.GlobalSecondaryIndexPropsV2(
            #         index_name="gsi",
            #         partition_key=dynamodb.Attribute(name="pk", type=dynamodb.AttributeType.STRING)
            #     )
            # ]
            contributor_insights=True,
        )