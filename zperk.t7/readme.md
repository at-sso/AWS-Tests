this actually doesn't work lmfao (won't fix)

# Book Store Chatbot

This Python application interacts with an Amazon Lex bot and an AWS Lambda function to provide a functional chatbot for the internal team of a Book Store. The chatbot allows users to register new users and edit existing users via simple conversational commands.

## Table of Contents

- [Book Store Chatbot](#book-store-chatbot)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Architecture](#architecture)
  - [Setup Instructions](#setup-instructions)
    - [Prerequisites](#prerequisites)
    - [Amazon Lex Bot Setup](#amazon-lex-bot-setup)
    - [AWS Lambda Function Setup](#aws-lambda-function-setup)
  - [How It Works](#how-it-works)
  - [Running the Application](#running-the-application)
  - [AWS Services](#aws-services)
    - [Amazon Lex](#amazon-lex)
    - [AWS Lambda](#aws-lambda)
  - [Important Considerations](#important-considerations)

## Overview

The application is designed to interact with an Amazon Lex bot, which processes natural language input from users. The bot handles two main intents: registering a new user and editing an existing user. When these intents are triggered, the Lex bot communicates with an AWS Lambda function that processes the logic for user management.

## Architecture

1. **User Input**: The user interacts with the chatbot via the Python command-line interface (CLI).
2. **Amazon Lex**: The Python application sends the user's input to an Amazon Lex bot using the `boto3` library.
3. **AWS Lambda**: Depending on the user's intent (e.g., RegisterUserIntent, EditUserIntent), the Lex bot triggers an AWS Lambda function. This Lambda function performs the necessary actions, such as registering or editing a user.
4. **Response**: The Lambda function sends a response back to the Lex bot, which is then returned to the user through the Python application.

## Setup Instructions

### Prerequisites

- **AWS Account**: Ensure you have an AWS account.
- **AWS CLI**: Set up AWS CLI on your local machine and configure it with your credentials.
- **Python**: Ensure Python 3.x is installed on your machine.
- **Boto3**: Install the AWS SDK for Python (Boto3) using the command:

  ```bash
  pip install boto3
  ```

### Amazon Lex Bot Setup

1. **Create Intents**: Define the `RegisterUserIntent` and `EditUserIntent` in Amazon Lex. These intents should have slots to capture user information like username and email.
2. **Create the Bot**: Create the Lex bot and include the intents you've defined.
3. **Set Up Fulfillment**: For both intents, configure a CodeHook that triggers an AWS Lambda function for processing.

### AWS Lambda Function Setup

1. **Create a Lambda Function**: In AWS Lambda, create a new function that handles the logic for user registration and editing.
2. **Lambda Code**: Use the provided Lambda function code to process the events sent by Lex. This function should take user data from Lex, perform the required operation (e.g., store in a database), and return a response.
3. **IAM Role**: Ensure the Lambda function has the necessary IAM role permissions to interact with other AWS services if needed.

## How It Works

1. **User Interaction**: The user types a message into the Python CLI, such as "Register a user with username John and email john@example.com."
2. **Lex Bot Processing**: The message is sent to the Amazon Lex bot using the `post_text` method from the Boto3 `lex-runtime` client. Lex processes the input based on predefined intents.
3. **Intent Handling**: If the input matches an intent, Lex triggers the associated Lambda function.
4. **Lambda Execution**: The Lambda function processes the input, performs the necessary operations (e.g., storing the user in a database), and returns a result.
5. **Response Delivery**: Lex sends the Lambda function's response back to the Python application, which is displayed to the user.

## Running the Application

1. Clone the repository containing the Python script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script:

   ```bash
   python chatbot.py
   ```

4. Follow the on-screen instructions to interact with the chatbot.

## AWS Services

### Amazon Lex

Amazon Lex is a service for building conversational interfaces using voice and text. In this application, Lex is responsible for interpreting user input and determining the correct intent to execute (registering or editing a user).

- **Intents**: Intents are predefined goals that the user can achieve by interacting with the bot. Each intent is associated with specific user requests.
- **Slots**: Slots are used to capture specific pieces of information from the user, such as usernames or email addresses.

### AWS Lambda

AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. In this application, Lambda functions are used to handle the logic for user registration and editing when triggered by the Lex bot.

- **CodeHook**: A Lambda function is connected to Lex using a CodeHook, which is triggered when Lex determines that an intent should be fulfilled.

## Important Considerations

- **Security**: Ensure that IAM roles and permissions are properly configured to secure your AWS resources.
- **Error Handling**: Consider adding more robust error handling both in the Lambda function and in the Python application.
- **Scalability**: The application can be scaled by integrating more intents and enhancing the logic within the Lambda functions.
