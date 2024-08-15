#!/bin/bash

set -e

table_name="$1"

aws dynamodb create-table \
    --table-name "$table_name" \
    --attribute-definitions AttributeName=user_id,AttributeType=S AttributeName=book_id,AttributeType=S \
    --key-schema AttributeName=user_id,KeyType=HASH AttributeName=book_id,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

if [ $? -eq 0 ]; then
    echo "DynamoDB table created successfully."
else
    echo "Failed to create DynamoDB table." >&2
    exit 1
fi
