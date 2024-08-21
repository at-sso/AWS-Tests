import aws_lex
import aws_lambda
import boto3

# Initialize the Lex client
client = aws_lambda.client


def main():
    # Create the DynamoDB table if it doesn't exist
    aws_lambda.create_dynamodb_table()

    # Set up the Lex bot with intents
    aws_lex.setup_lex_bot()

    # Deploy the Lambda function
    lambda_client = boto3.client("lambda")

    with open("aws_lambda.py", "rb") as f:
        lambda_code = f.read()

    try:
        response = lambda_client.create_function(
            FunctionName="BookStoreUserManagementFunction",
            Runtime="python3.9",
            Role=aws_lex.lambda_arn,
            Handler="aws_lambda.lambda_handler",
            Code={"ZipFile": lambda_code},
            Timeout=15,
            MemorySize=128,
            Publish=True,
        )
        print("Lambda function created successfully:", response["FunctionArn"])
    except lambda_client.exceptions.ResourceConflictException:
        print("Lambda function already exists.")

    # Note: Ensure the Lambda function's ARN is updated in the Lex bot intents configuration


if __name__ == "__main__":
    main()
