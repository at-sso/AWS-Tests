import sys
import os
import json
import boto3
from botocore.exceptions import ClientError
from typing import Any, Dict, Union

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.secrets"))
)

from clownkey import dynamo_secret  # type: ignore

dynamodb: Any = boto3.resource("dynamodb")
table = dynamodb.Table(dynamo_secret)


def lambda_handler(event: Any, context: Any) -> Dict[str, Union[str, int]]:
    user_id = event["user_id"]
    book_id = event["book_id"]
    loan_date = event["loan_date"]

    try:
        response: Any = table.put_item(
            Item={
                "user_id": user_id,
                "book_id": book_id,
                "loan_date": loan_date,
            }
        )
        return {"statusCode": 200, "body": json.dumps("Loan recorded successfully!")}
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": json.dumps(
                f"Failed to record loan: {e.response['Error']['Message']}"
            ),
        }
