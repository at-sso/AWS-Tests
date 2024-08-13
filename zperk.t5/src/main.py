import sys
import os
import boto3
import json
from datetime import datetime
from typing import Callable, Dict, Any

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.secrets"))
)

from clownkey import dynamo_secret, flag_secrets, LE_SECRETS  # type: ignore

# Setup DynamoDB resource
dynamodb: Any = boto3.resource("dynamodb", region_name="us-east-1")
table_name = LE_SECRETS if flag_secrets else dynamo_secret
table = dynamodb.Table(dynamo_secret)


def deploy_data() -> None:
    # Create the DynamoDB table
    table: Any = dynamodb.create_table(
        TableName=dynamo_secret,
        KeySchema=[
            {"AttributeName": "UserID", "KeyType": "HASH"},  # Partition key
            {"AttributeName": "BookID", "KeyType": "RANGE"},  # Sort key
        ],
        AttributeDefinitions=[
            {"AttributeName": "UserID", "AttributeType": "S"},
            {"AttributeName": "BookID", "AttributeType": "S"},
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    )
    table.wait_until_exists()
    print(f"DynamoDB table {table_name} created successfully.")


def check_data() -> None:
    response: Any = table.scan()
    items: Any = response.get("Items", [])
    print(f"Data in {table_name}:")
    for item in items:
        print(json.dumps(item, indent=4))


def destroy_data() -> None:
    table.delete()
    print(f"DynamoDB table {table_name} deleted successfully.")


def borrow_book() -> None:
    user_id = input("Enter User ID: ")
    book_id = input("Enter Book ID: ")
    borrow_time = datetime.now().isoformat()

    # Insert record into DynamoDB
    table.put_item(
        Item={"UserID": user_id, "BookID": book_id, "BorrowTime": borrow_time}
    )
    print(f"User {user_id} borrowed book {book_id} at {borrow_time}.")


def list_borrowers() -> None:
    # Query DynamoDB for all users who borrowed books
    response = table.scan()
    items = response.get("Items", [])

    print("Users who have borrowed books:")
    for item in items:
        print(f"UserID: {item['UserID']}, BookID: {item['BookID']}")


def list_users_with_time() -> None:
    # Query DynamoDB for all users and their borrow times
    response = table.scan()
    items = response.get("Items", [])

    print("Users and their borrow times:")
    for item in items:
        print(
            f"UserID: {item['UserID']}, BookID: {item['BookID']}, BorrowTime: {item['BorrowTime']}"
        )


IntToFunctionDict = Dict[int, Callable[[], Any]]


def main() -> int:

    execute_debug: IntToFunctionDict = {
        1: deploy_data,
        2: check_data,
        3: destroy_data,
    }

    execute: IntToFunctionDict = {
        1: borrow_book,
        2: list_borrowers,
        3: list_users_with_time,
    }

    clearsrc = lambda: os.system("cls" if os.name == "nt" else "clear")

    def selector_is_invalid(selection: str) -> bool:
        if selection not in ["1", "2", "3"]:
            print("Select a valid input.")
            return True
        return False

    def execute_action(selection: str, actions: IntToFunctionDict) -> int:
        try:
            actions[int(selection)]()
            return 0
        except Exception as err:
            print(f"Error: {err}")
            return 1

    def debug_mode() -> int:
        while True:
            clearsrc()
            print("1. Deploy data\n2. Check data\n3. Destroy all data\n4. Return")
            selection: str = input("> ")
            if selection == "4":
                return 0
            if selector_is_invalid(selection):
                continue

            return execute_action(selection, execute_debug)

    a: int = 0

    while True:
        clearsrc()
        print(
            "1. Borrow a book\n"
            "2. List of users that borrowed books\n"
            "3. List of users and take in time\n"
            "4. Debug\n"
            "0. Exit"
        )
        selection: str = input("> ")

        if selection == "0":
            break
        if selection == "4":
            debug_mode()
            continue
        if selector_is_invalid(selection):
            continue

        a = execute_action(selection, execute)

    return a


if __name__ == "__main__":
    a = main()
    sys.exit(a)
