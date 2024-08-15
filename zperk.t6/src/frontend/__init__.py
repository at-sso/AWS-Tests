import boto3
import json
from typing import Any


def init() -> None:
    client: Any = boto3.client("lambda")

    response = client.invoke(
        FunctionName="RecordLoanFunction",
        Payload=json.dumps(
            {"user_id": "123", "book_id": "abc", "loan_date": "2024-08-14"}
        ),
    )

    response_payload = json.loads(response["Payload"].read())
    print(response_payload)
