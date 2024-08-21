# Image Recognition with Amazon Rekognition

This Python script uses the Amazon Rekognition service to analyze images and retrieve labels with confidence scores.

## Features

- **Image Selection:** Select images through a file dialog.
- **Amazon Rekognition Integration:** Detect labels in images using Amazon's Rekognition API.
- **Customizable Output:** View a simplified or full JSON response.
- **Error Handling:** Logs errors and provides fallback values for missing data.

## Prerequisites

- **Python 3.x** installed
- **Boto3** installed: `pip install boto3`
- **Tkinter** installed: Typically included with Python, but ensure it's available.

## Setup

1. Clone or download the project.
2. Ensure you have the necessary AWS credentials set up to access Rekognition.
3. Place the required secrets in the `.secrets` directory and adjust the paths as needed.

## Usage

1. Run the script:

   ```bash
   python3 ./zperk.t8/src/main.py -H -w
   ```

2. Select an image from the dialog.
3. Choose whether to see the full JSON response or just a summary.

## Notes

- This script defaults to images located in [`./zperk.t8/src/img`](./src/img).
- Ensure that your AWS credentials have the appropriate permissions to use Rekognition.
