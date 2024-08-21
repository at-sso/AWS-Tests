__all__ = [
    "DOT_SECRETS_FILE",
    "ACCESS_KEYS_FILE",
    "CREDENTIALS_FILE",
    "LE_SECRETS",
    "dot_secrets",
    "unsecure",
    "rds_secrets",
    "s3_secrets",
    "dynamo_secret",
    "lambda_id",
    "lambda_role",
    "lambda_arn",
    "dot_secrets_formatted",
    "this_path",
    "easter_egg",
    "dot_secrets_path",
    "access_keys_path",
    "credentials_path",
]

import os
from typing import Any, Dict
from typing_extensions import LiteralString

DOT_SECRETS_FILE = ".secrets"
ACCESS_KEYS_FILE = "accessKeys.gpg.csv"
CREDENTIALS_FILE = "credentials.gpg.csv"
LE_SECRETS: LiteralString = "[secrets]"
"""Literal '[secrets]' string."""

########################### You can update this with your own credentials. ###########################

dot_secrets: Dict[str, Any] = {
    "unsecure": "your generic password",
    "RDS": {
        "username": "admin",
        "endpoint": "your rds endpoint",
    },
    "S3": {
        "bucket_name": "your bucket name",
        "bucket_list": "aws s3 ls s3://{name} --recursive",
    },
    "DynamoDB": "DynamoDB",
    "LambdaRole": {
        "id": "123456789012",
        "role": "service-role/",
        "arn": "arn:aws:lambda:",
    },
}
"""The '.secrets' JSON credentials."""

########################### Modifying anything after this takes no effect. ###########################

unsecure: str = ""
"""Generic password I use across all password dependant AWS projects."""

rds_secrets: Dict[str, str] = {}
"""Array with 'username' and 'endpoint' keys."""

s3_secrets: Dict[str, str] = {}
"""Array with 'bucket_name' and 'bucket_list' keys."""

dynamo_secret: str = ""
"""Generic DynamoDB name."""

lambda_id: str = ""
"""Generic lambda account id."""

lambda_role: str = ""
"""Generic lambda role."""

lambda_arn: str = ""
"""Generic lambda ARN."""

dot_secrets_formatted: str = ""
"""The '.secrets' JSON credentials, formatted. Useful for printing."""

this_path: str = os.path.abspath(".").replace("\\", "/")
"""Returns the current absolute path."""

easter_egg: str = f"{this_path}/.secrets/private"
"""Returns the standardized path for the easter egg."""

dot_secrets_path: str = f"{easter_egg}/out/{DOT_SECRETS_FILE}"
"""Returns the '.secret' absolute path."""

access_keys_path: str = f"{easter_egg}/out/{ACCESS_KEYS_FILE}"
"""Returns the 'accessKeys' absolute path."""

credentials_path: str = f"{easter_egg}/out/{CREDENTIALS_FILE}"
"""Returns the 'credentials' absolute path."""
