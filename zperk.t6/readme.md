# AWS Lambda Book Loan Management

This project provides a simple AWS Lambda-based backend for managing user and book loan records using DynamoDB. The setup includes bash scripts for creating the necessary AWS resources, deploying the Lambda function, and testing the setup.

## Project Structure

```
.
├── README.md
└── src
    ├── aws
    │   ├── create.sh          # Script to create DynamoDB table
    │   ├── deploy.sh          # Script to deploy Lambda function
    │   ├── test.sh            # Script to test the Lambda function
    │   └── zip.sh             # Script to package Lambda function
    ├── backend
    │   └── __init__.py        # Backend logic (Lambda function code)
    ├── frontend
    │   └── __init__.py        # Frontend code to interact with the Lambda function
    └── main.py                # Main script to automate the setup and test
```

## Prerequisites

1. **AWS CLI**: Ensure that you have AWS CLI installed and configured with the necessary permissions.
2. **Python 3.x**: Required for running the `main.py` script and any Python code in the `frontend` and `backend`.
3. **IAM Role**: Create an IAM role with the following policies:
   - `AWSLambdaBasicExecutionRole`
   - `AmazonDynamoDBFullAccess`
     Use the ARN of this role in the deployment script.

## Setup and Deployment

Follow these steps to set up and deploy the project:

### 1. Create the DynamoDB Table

Navigate to the project directory and run the `create.sh` script to create the DynamoDB table:

```bash
bash src/aws/create.sh
```

This will create a `LoansTable` in DynamoDB with `user_id` and `book_id` as the primary keys.

### 2. Package the Lambda Function

Run the `zip.sh` script to package the Lambda function:

```bash
bash src/aws/zip.sh
```

This will create a `fn.zip` file containing the Lambda function code.

### 3. Deploy the Lambda Function

Deploy the Lambda function using the `deploy.sh` script:

```bash
bash src/aws/deploy.sh <your-account-id> <your-lambda-execution-role>
```

Replace `<your-account-id>` and `<your-lambda-execution-role>` with your actual AWS account ID and the IAM role ARN created earlier.

### 4. Test the Lambda Function

After deployment, you can test the Lambda function by running the `test.sh` script:

```bash
bash src/aws/test.sh
```

This script invokes the Lambda function with a test payload and prints the response.

### 5. Run the Main Script

To automate the entire setup process and ensure everything works correctly, run the `main.py` script:

```bash
python3 src/main.py
```

This script will sequentially execute all the bash scripts, handle errors, and test the frontend functionality.

## Frontend Usage

The frontend code in `src/frontend/__init__.py` interacts with the Lambda function. Customize it according to your requirements and ensure it correctly invokes the Lambda function using the appropriate AWS SDK (e.g., `boto3`).

## Notes

- Make sure your AWS credentials are correctly configured before running these scripts.
- Adjust the IAM policies and roles as needed to meet your security requirements.

## Troubleshooting

- **Invalid Base64 Errors**: Ensure that the payload sent to the Lambda function is correctly formatted and that the function itself does not require base64 encoding unless explicitly necessary.
- **Permission Issues**: Double-check that the IAM role attached to your Lambda function has the necessary permissions to access DynamoDB and CloudWatch.
