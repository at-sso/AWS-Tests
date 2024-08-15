#!/bin/bash

set -e

abspath="$1"

zip "$abspath"/init.zip "$abspath"/__init__.py

if [ $? -eq 0 ]; then
    echo "Function zipped successfully."
else
    echo "Failed to zip the function." >&2
    exit 1
fi
