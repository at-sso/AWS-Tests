import boto3
import os
import sys
import json
import tkinter as tk
from tkinter import filedialog
from typing import Any, Dict
from typing_extensions import NoReturn

# Add secret path to sys.path to access 'clownkey'.
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.secrets"))
)

from clownkey import this_path  # type: ignore


def __log_error(name: str, e: Any = None, message: str = "") -> NoReturn:
    """Function to log errors with optional exception details"""
    if e:
        print(f"Raised exception from '{name}'. > {e}")
    else:
        print(f"Error from '{name}'. > {message}")
    sys.exit(1)


def select_image() -> str:
    """Function to display a file dialog and select an image"""
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    return filedialog.askopenfilename(
        initialdir=f"{this_path}/zperk.t8/src/img",  # Set initial directory
        title="Select Image",  # Dialog title
        filetypes=(("Image files", "*.jpg *.png"),),  # File types allowed
    )


def recognize_image(image_path: str) -> Dict[str, Any]:
    """Function to send the selected image to Amazon Rekognition and return the response"""
    print(f"Operation started... Please wait!")
    try:
        client: Any = boto3.client("rekognition")  # Initialize Rekognition client
        with open(image_path, "rb") as image_file:  # Open the image file in binary mode
            print("Done.")
            return client.detect_labels(
                Image={"Bytes": image_file.read()}, MaxLabels=10
            )
    except Exception as e:
        __log_error(recognize_image.__name__, e)  # Log error if there's an exception


def response_handler(response: Dict[str, Any], show_full_json: bool = False) -> None:
    """Function to format and print the JSON response from Rekognition"""
    if show_full_json:  # Print the full JSON response if requested
        print(json.dumps(response, indent=4))
        return

    # Extract labels from the response
    labels: Any = response.get("Labels", [])
    if not labels:  # Log error if no labels found
        __log_error(response_handler.__name__, message="No labels recognized.")

    # Iterate through the first three labels
    for label in labels[:3]:
        # Get the label name, default to 'Null' if not found
        name: Any = label.get("Name", "Null")
        # Format confidence, default to 'Null'
        confidence: str = f"{label.get('Confidence', 'Null'):.2f}%"

        print(f"Name: {name}")
        print(f"Confidence: {confidence}")

        # Iterate through optional array keys and print their contents
        for array_key in ["Instances", "Parents", "Aliases", "Categories"]:
            items: Any = label.get(array_key, [])
            for item in items:
                for k, v in item.items():
                    # Print key-value pairs, defaulting to 'Null' if empty
                    print(f"  {k}: {v if v else 'Null'}")
        print()  # Prints a newline for separation


# baby you got something in your nooooseee
# sniffin that k do you feel the hole?

if __name__ == "__main__":
    # Select an image
    img_path: str = select_image()

    # Check if an image was selected
    if not img_path:
        __log_error("main", message="Operation canceled.")

    response: Dict[str, Any] = recognize_image(img_path)
    show_full_json: bool = (
        input("Do you want to see the full JSON response? (y/n): ").lower() == "y"
    )
    response_handler(response, show_full_json)
