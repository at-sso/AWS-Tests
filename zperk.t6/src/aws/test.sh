#!/bin/bash

set -e

# Convert JSON payload to base64
payload=$(echo -n '{"user_id": "123", "book_id": "abc", "loan_date": "2024-08-14"}' | base64)

aws lambda invoke \
    --function-name RecordLoanFunction \
    --payload "$payload" \
    response.json

if [ $? -eq 0 ]; then
    echo "Lambda function invoked successfully. Response:"
    cat response.json
else
    echo "Failed to invoke Lambda function." >&2
    exit 1
fi
