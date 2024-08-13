import os
import subprocess
import sys
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from typing import Any, Dict, Callable, List
from PIL import Image
from PIL.ImageFile import ImageFile
from PIL.Image import Image as ImageType

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.secrets"))
)

from clownkey import this_path, s3_secrets, flag_secrets  # type: ignore

# Constants
BUCKET_NAME: str = s3_secrets["bucket_name"]  # type: ignore[reportUnknownVariableType]
BUCKET_LIST_CMD: str = s3_secrets["bucket_list"].replace("{name}", BUCKET_NAME) # type: ignore[reportUnknownMemberType]
DOWNLOAD_PATH: str = f"{this_path}/env/download"
LOCAL_FILES_PATH: str = f"{this_path}/zperk.t3/src/img"
MAIN_MENU: str = (
    "1. Upload to S3\n"
    "2. Download from S3\n"
    "3. Check S3 file list\n"
    "4. Check local file list\n"
    "5. Delete all files in S3\n"
    "6. Render file from local downloads\n"
    "0. Exit"
)


def file_list_from_s3() -> None:
    """Shows a list of the files stored in the S3 bucket."""
    subprocess.run(BUCKET_LIST_CMD, shell=True)


def file_tree(start_path: str, indent_level: int = 0) -> None:
    """Displays the file tree starting from a specified path."""
    try:
        with os.scandir(start_path) as entries:
            for entry in entries:
                print("  " * indent_level + f"- {entry.name}")
                if entry.is_dir():
                    file_tree(entry.path, indent_level + 1)
    except PermissionError:
        print("  " * indent_level + "[Permission Denied]")


def upload_to_s3(file_name: str, bucket: str, key: str, s3_client: Any) -> None:
    """Uploads a file to an S3 bucket."""
    try:
        s3_client.upload_file(file_name, bucket, key)
        print(f"File {file_name} uploaded to {bucket} with key {key}.")
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except (NoCredentialsError, PartialCredentialsError):
        print("S3 credentials not available or incomplete.")
    except Exception as e:
        print(f"An error occurred: {e}")


def download_from_s3(download_path: str, bucket: str, key: str, s3_client: Any) -> None:
    """Downloads a file from an S3 bucket."""
    try:
        s3_client.download_file(bucket, key, download_path)
        print(f"File {key} downloaded from {bucket} to {download_path}.")
    except (NoCredentialsError, PartialCredentialsError):
        print("S3 credentials not available or incomplete.")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_all_s3_files(bucket_name: str, s3_client: Any) -> None:
    """Deletes all files in an S3 bucket."""
    show_bucket: str = "[secret]" if flag_secrets else bucket_name
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if "Contents" not in response:
            print(f"No files found in bucket: {show_bucket}")
            return

        keys = [{"Key": obj["Key"]} for obj in response["Contents"]]

        if keys:
            s3_client.delete_objects(Bucket=bucket_name, Delete={"Objects": keys})
            print(f"Deleted {len(keys)} objects from bucket: {show_bucket}")
    except Exception as e:
        print(f"An error occurred: {e}")


def image_to_ascii(file_name: str, width: int = 100) -> str:
    """Converts an image to ASCII art."""
    file_path = f"{DOWNLOAD_PATH}/{file_name}"
    try:
        image_obj: ImageFile = Image.open(file_path)
        image: ImageType = image_obj.resize(
            (width, int(image_obj.height / image_obj.width * width))
        ).convert("L")

        ascii_chars = "@%#*+=-:. "
        pixels: List[int] = list(image.getdata())  # type: ignore[reportArgumentType]
        ascii_str: str = "".join([ascii_chars[pixel // 32] for pixel in pixels])

        ascii_image: str = "\n".join(
            [ascii_str[i : i + width] for i in range(0, len(ascii_str), width)]
        )
        return ascii_image

    except Exception as e:
        print(f"Error converting image to ASCII: {e}")
        return "Render Error"


def main() -> int:
    s3_client: Any = boto3.client("s3")  # type: ignore[reportUnknownMemberType]

    actions: Dict[int, Callable[..., None]] = {
        1: lambda file_key: upload_to_s3(
            f"{LOCAL_FILES_PATH}/{file_key}", BUCKET_NAME, file_key, s3_client
        ),
        2: lambda file_key: download_from_s3(
            f"{DOWNLOAD_PATH}/{file_key}", BUCKET_NAME, file_key, s3_client
        ),
        3: file_list_from_s3,
        4: lambda: file_tree(LOCAL_FILES_PATH),
        5: lambda: delete_all_s3_files(BUCKET_NAME, s3_client),
    }

    print(MAIN_MENU)
    while True:
        try:
            selector: str = input("> ")
            if selector == "0":  # Exit
                break
            elif selector == "6":  # Render local image.
                file_tree(DOWNLOAD_PATH)
                ascii_art = image_to_ascii(input("Filename: "))
                print(f"{ascii_art}\n\n\n{MAIN_MENU}")
            elif selector in ["1", "2"]:  # Upload or download from S3.
                actions[int(selector)](input("Filekey: "))
            elif selector in ["3", "4", "5"]:  # Check files, or delete in case of '5'.
                actions[int(selector)]()

        except Exception as e:
            print(f"An error occurred: {e}")
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
