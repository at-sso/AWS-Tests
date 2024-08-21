import sys
import os
import boto3
from typing import Any

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.secrets"))
)

from clownkey import dynamo_secret, LE_SECRETS, flag_secrets  # type: ignore


# Initialize DynamoDB
dynamodb: Any = boto3.resource("dynamodb")
client: Any = boto3.client("lex-runtime")
table_name = LE_SECRETS if flag_secrets else dynamo_secret
global_table: Any = None


def create_dynamodb_table() -> None:
    global global_table
    try:
        # Check if the table already exists
        global_table = dynamodb.Table(dynamo_secret)
        global_table.load()
        print(f"Table '{table_name}' already exists.")
    except Exception:
        # Create the table if it doesn't exist
        print(f"Creating table '{table_name}'...")
        global_table = dynamodb.create_table(
            TableName=dynamo_secret,
            KeySchema=[{"AttributeName": "Username", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "Username", "AttributeType": "S"}],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
        global_table.wait_until_exists()
        print(f"Table '{table_name}' created successfully.")


def lambda_handler(event: Any):
    intent_name = event["currentIntent"]["name"]

    if intent_name == "RegisterUserIntent":
        return handle_register_user(event)
    elif intent_name == "EditUserIntent":
        return handle_edit_user(event)

    return {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Failed",
            "message": {
                "contentType": "PlainText",
                "content": "Sorry, I couldn't understand the request.",
            },
        }
    }


def handle_register_user(event: Any):
    username = event["currentIntent"]["slots"]["Username"]
    email = event["currentIntent"]["slots"]["Email"]

    # Check if the user already exists
    response = global_table.get_item(Key={"Username": username})
    if "Item" in response:
        return {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": f"User {username} is already registered.",
                },
            }
        }

    # Register new user
    global_table.put_item(Item={"Username": username, "Email": email})

    return {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": f"User {username} has been registered with email {email}.",
            },
        }
    }


def handle_edit_user(event: Any):
    username = event["currentIntent"]["slots"]["Username"]
    new_email = event["currentIntent"]["slots"]["NewEmail"]

    # Check if the user exists
    response = global_table.get_item(Key={"Username": username})
    if "Item" not in response:
        return {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": f"User {username} does not exist.",
                },
            }
        }

    # Update user's email
    global_table.update_item(
        Key={"Username": username},
        UpdateExpression="set Email = :e",
        ExpressionAttributeValues={":e": new_email},
    )

    return {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": f"User {username} has been updated with new email {new_email}.",
            },
        }
    }
