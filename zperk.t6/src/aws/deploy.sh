#!/bin/bash

set -e

account_id="$1"
lambda_execution_role="$2"
zip_abspath="$3"

if [ -z "$account_id" ] || [ -z "$lambda_execution_role" ]; then
    echo "Account ID and Lambda execution role must be provided." >&2
    exit 1
fi

if [ -z "$zip_abspath" ]; then
    echo "Zip absolute path must be provided."
    exit 2
fi

aws lambda create-function \
    --function-name RecordLoanFunction \
    --runtime python3.10 \
    --role arn:aws:iam::"$account_id":role/"$lambda_execution_role" \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://"$zip_abspath"

if [ $? -eq 0 ]; then
    echo "Lambda function deployed successfully."
else
    echo "Failed to deploy Lambda function." >&2
    exit 1
fi
