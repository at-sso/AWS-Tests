import sys
import json
from datetime import datetime
from typing import Callable, Dict, Any, List
from helpers import *


def scan_table() -> List[Dict[str, Any]]:
    global extr_msg
    try:
        response = table.scan()
        return response.get("Items", [])
    except Exception as e:
        extr_msg = f"Error scanning table: {e}"
        return []


def deploy_data() -> None:
    global extr_msg
    try:
        table = dynamodb.create_table(
            TableName=dynamo_secret,
            KeySchema=[
                {"AttributeName": "UserID", "KeyType": "HASH"},
                {"AttributeName": "BookID", "KeyType": "RANGE"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "UserID", "AttributeType": "S"},
                {"AttributeName": "BookID", "AttributeType": "S"},
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
        table.wait_until_exists()
        extr_msg = f"DynamoDB table {table_name} created successfully."
    except Exception as e:
        extr_msg = f"Error creating table: {e}"


def check_data() -> None:
    global extr_msg
    items = scan_table()
    extr_msg = f"Data in {table_name}:"
    for item in items:
        extr_msg = json.dumps(item, indent=4)


def destroy_data() -> None:
    global extr_msg
    try:
        table.delete()
        extr_msg = f"DynamoDB table {table_name} deleted successfully."
    except Exception as e:
        extr_msg = f"Error deleting table: {e}"


def borrow_book() -> None:
    global extr_msg
    user_id = id_handler("User")
    book_id = id_handler("Book")

    borrow_time = datetime.now().isoformat()

    try:
        table.put_item(
            Item={"UserID": user_id, "BookID": book_id, "BorrowTime": borrow_time}
        )
        extr_msg = f"User {user_id} borrowed book {book_id} at {borrow_time}."
    except Exception as e:
        extr_msg = f"Error borrowing book: {e}"


def list_borrowers() -> None:
    global extr_msg
    items = scan_table()

    extr_msg = "Users who have borrowed books:"
    for item in items:
        extr_msg = f"UserID: {item['UserID']}, BookID: {item['BookID']}"


def list_users_with_time() -> None:
    global extr_msg
    items = scan_table()

    extr_msg = "Users and their borrow times:"
    for item in items:
        extr_msg = f"UserID: {item['UserID']}, BookID: {item['BookID']}, BorrowTime: {item['BorrowTime']}"


def selector_is_invalid(selection: str) -> bool:
    global extr_msg
    if selection not in ["1", "2", "3"]:
        extr_msg = "Select a valid input."
        return True
    return False


def execute_action(selection: str, actions: Dict[int, Callable[[], None]]) -> bool:
    global extr_msg
    try:
        actions[int(selection)]()
        return False
    except Exception as e:
        extr_msg = f"Execution error: {e}"
        return True


def debug_mode() -> int:
    global extr_msg
    while True:
        clearsrc()
        print(
            "1. Deploy data\n2. Check data\n3. Destroy all data\n4. Return\n", extr_msg
        )
        selection = input("> ")
        if selection == "4":
            extr_msg = ""
            return 0
        if selector_is_invalid(selection):
            continue

        actions = action_helper(deploy_data, check_data, destroy_data)

        if execute_action(selection, actions):
            continue


def main() -> int:
    while True:
        clearsrc()
        print(
            "1. Borrow a book\n"
            "2. List of users that borrowed books\n"
            "3. List of users and take in time\n"
            "4. Debug\n"
            "0. Exit\n",
            extr_msg,
        )
        selection = input("> ")

        if selection == "0":
            break
        if selection == "4":
            debug_mode()
            continue
        if selector_is_invalid(selection):
            continue

        actions = action_helper(borrow_book, list_borrowers, list_users_with_time)
        if execute_action(selection, actions):
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
