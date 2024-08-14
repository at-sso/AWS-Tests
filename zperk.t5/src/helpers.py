__all__ = [
    "dynamo_secret",
    "flag_secrets",
    "LE_SECRETS",
    "clearsrc",
    "id_handler",
    "action_helper",
    "dynamodb",
    "table_name",
    "table",
    "extr_msg",
]

import os
import sys
import boto3
from typing import Callable, Dict, Any

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.secrets"))
)

from clownkey import dynamo_secret, flag_secrets, LE_SECRETS  # type: ignore

# Setup DynamoDB resource
dynamodb: Any = boto3.resource("dynamodb", region_name="us-east-1")
table_name = LE_SECRETS if flag_secrets else dynamo_secret
table = dynamodb.Table(dynamo_secret)
extr_msg: str = ""


def clearsrc() -> None:
    """Clears the screen"""
    os.system("cls" if os.name == "nt" else "clear")


def id_handler(id_type: str = "") -> str:
    """Handles the correct input of IDs."""
    a: int = 0
    while True:
        try:
            a = int(input(f"Enter {id_type + ' ' if id_type else ''}ID: "))
        except ValueError as err:
            print(err)
            continue
        else:
            return str(a)


def action_helper(*actions: Callable[[], None]) -> Dict[int, Callable[[], None]]:
    """Returns a dictionary of callable functions."""
    if not (1 <= len(actions) <= 3):
        raise IndexError("The number of actions must be between 1 and 3.")
    return {i + 1: action for i, action in enumerate(actions)}
