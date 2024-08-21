import os
import sys
from typing import Any
import boto3

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.secrets"))
)

from clownkey import lambda_arn  # type: ignore


def setup_lex_bot():
    client_lex: Any = boto3.client("lex-models")

    # Create the RegisterUserIntent
    register_intent_response = client_lex.put_intent(
        name="RegisterUserIntent",
        sampleUtterances=[
            "I want to register a new user",
            "Register a user with username {Username}",
        ],
        slots=[
            {
                "name": "Username",
                "slotConstraint": "Required",
                "slotType": "AMAZON.Person",
                "slotTypeVersion": "$LATEST",
                "valueElicitationPrompt": {
                    "messages": [
                        {"contentType": "PlainText", "content": "What is the username?"}
                    ],
                    "maxAttempts": 3,
                },
            },
            {
                "name": "Email",
                "slotConstraint": "Required",
                "slotType": "AMAZON.EmailAddress",
                "slotTypeVersion": "$LATEST",
                "valueElicitationPrompt": {
                    "messages": [
                        {
                            "contentType": "PlainText",
                            "content": "What is the email address?",
                        }
                    ],
                    "maxAttempts": 3,
                },
            },
        ],
        fulfillmentActivity={
            "type": "CodeHook",
            "codeHook": {
                "uri": lambda_arn,
                "messageVersion": "1.0",
            },
        },
    )

    # Create the EditUserIntent
    edit_intent_response = client_lex.put_intent(
        name="EditUserIntent",
        sampleUtterances=[
            "I want to edit user {Username}",
            "Edit the user with username {Username}",
        ],
        slots=[
            {
                "name": "Username",
                "slotConstraint": "Required",
                "slotType": "AMAZON.Person",
                "slotTypeVersion": "$LATEST",
                "valueElicitationPrompt": {
                    "messages": [
                        {"contentType": "PlainText", "content": "What is the username?"}
                    ],
                    "maxAttempts": 3,
                },
            },
            {
                "name": "NewEmail",
                "slotConstraint": "Required",
                "slotType": "AMAZON.EmailAddress",
                "slotTypeVersion": "$LATEST",
                "valueElicitationPrompt": {
                    "messages": [
                        {
                            "contentType": "PlainText",
                            "content": "What is the new email address?",
                        }
                    ],
                    "maxAttempts": 3,
                },
            },
        ],
        fulfillmentActivity={
            "type": "CodeHook",
            "codeHook": {
                "uri": lambda_arn,
                "messageVersion": "1.0",
            },
        },
    )

    # Create the bot with both intents
    bot_response = client_lex.put_bot(
        name="BookStoreInternalBot",
        description="Bot to register and edit users for the Book Store company",
        intents=[
            {"intentName": "RegisterUserIntent", "intentVersion": "$LATEST"},
            {"intentName": "EditUserIntent", "intentVersion": "$LATEST"},
        ],
        clarificationPrompt={
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "Sorry, I didn't understand that. Can you please repeat?",
                }
            ],
            "maxAttempts": 2,
        },
        abortStatement={
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "I'm sorry, I'm unable to assist you at the moment.",
                }
            ]
        },
        idleSessionTTLInSeconds=300,
        voiceId="Joanna",
        locale="en-US",
        childDirected=False,
    )

    print("Lex Bot Created:", bot_response)
