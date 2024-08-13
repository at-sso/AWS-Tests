__all__ = [
    "this_path",
    "easter_egg",
    "dot_secrets",
    "access_keys",
    "credentials",
    "dot_secrets_formatted",
]

import subprocess
import json
import os
import platform
import pandas as pd
from pandas import DataFrame
from getpass import getpass as gp
from typing import Any, Dict
from typing_extensions import LiteralString

from flags import *

# Installs Gpg4win on Windows if not already installed.
if platform.system() == "Windows" and not flag_win:
    print("Trying to install 'Gpg4win'. This tool is needed to decrypt the files.")
    subprocess.run("winget install --id GnuPG.Gpg4win")

this_path: str = os.path.abspath(".").replace("\\", "/")
easter_egg: str = f"{this_path}/.secrets/private"
"""Returns the standardized path for the easter egg."""
print("This Path ->", this_path)
print("Easter Eggs ->", easter_egg)

try:
    # Ensure the download directory exists
    os.mkdir(os.path.join(f"{this_path}/env", f"{this_path}/env/download"))
except:  # The directory does exist. I don't know why they raise an exception in this case like wtf
    pass


def __load_csv(abspath: str, mask_column: str = "") -> pd.DataFrame:
    """Loads a CSV file and optionally masks a specific column."""
    if not abspath:
        raise ValueError(f"{__load_csv.__name__}: An absolute path must be provided.")

    df: pd.DataFrame = pd.read_csv(abspath)  # Load the CSV file

    if mask_column:
        df[mask_column] = df[mask_column].apply(lambda x: "****" + x[-4:])

    return df


def __decrypt(passphrase: str, filename: str, is_csv: bool = False) -> str:
    """
    Decrypts a file using GPG and returns the output file path.

    passphrase: Passphrase for decryption.
    filename: Name of the file to decrypt.
    is_csv: Appends '.csv' to the output file name if True.
    """
    in_file: str = f"{easter_egg}/{filename}"
    out_file: str = f"{easter_egg}/out/{filename + ('.csv' if is_csv else '')}"

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(out_file), exist_ok=True)

    try:
        result = subprocess.run(
            [
                "gpg",
                "--batch",
                "--yes",
                "--passphrase",
                passphrase,
                "--output",
                out_file,
                "--decrypt",
                in_file,
            ],
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode != 0 or not os.path.exists(out_file):
            raise FileNotFoundError(f"Decryption failed: {result.stderr}")
    except Exception as e:
        raise RuntimeError(
            f"Error during decryption:\n{e}\n\n"
            f"Debug Info:\n- Input: '{in_file}'\n- Output: '{out_file}'"
        )

    return out_file


def __files_exist() -> bool:
    """Checks if the required decrypted files exist."""
    return all(
        os.path.exists(path)
        for path in [
            f"{easter_egg}/out/.secrets",
            f"{easter_egg}/out/accessKeys.gpg.csv",
            f"{easter_egg}/out/credentials.gpg.csv",
        ]
    )


# Paths to the decrypted files
__dot_secrets: str = f"{easter_egg}/out/.secrets"
__access_keys: str = f"{easter_egg}/out/accessKeys.gpg.csv"
__credentials: str = f"{easter_egg}/out/credentials.gpg.csv"

dot_secrets: Dict[str, Any] = {}
"""The '.secrets' JSON credentials."""
dot_secrets_formatted: str = ""
"""The '.secrets' JSON credentials, formatted."""
LE_SECRETS: LiteralString = "[secrets]"
"""The literal '[secrets]' string."""

# Try to load the '.secrets' file if it exists
try:
    with open(__dot_secrets, "r") as file:
        dot_secrets = json.load(file)
except FileNotFoundError:  # The file wasn't encrypted yet.
    pass
finally:
    dot_secrets_formatted = json.dumps(dot_secrets, indent=4) if dot_secrets else ""


# If the required files don't already exist, start the operation
if not __files_exist():
    # Helper flag to identify if user input is needed to complete the operation
    input_passphrase: bool = False

    # If the decrypt flag was set, set the path variables.
    if flag_decrypt:
        try:
            __dot_secrets = __decrypt(flag_decrypt[0], ".secrets")
            __access_keys = __decrypt(flag_decrypt[1], "accessKeys.gpg", True)
            __credentials = __decrypt(flag_decrypt[2], "credentials.gpg", True)
        except Exception as e:
            print(f"An error occurred:{e}\nTrying to get passphrases from user input.")
            input_passphrase = True
    else:
        input_passphrase = True

    # Either an error occurred or `flag_decrypt` was not set.
    if input_passphrase:
        try:
            print("Note: `getpass` function is being used. Input IS being received.")
            __dot_secrets = __decrypt(gp(".secrets: "), ".secrets")
            __access_keys = __decrypt(gp("accessKeys: "), "accessKeys.gpg", True)
            __credentials = __decrypt(gp("credentials: "), "credentials.gpg", True)
            # Once everything is set, get the decrypted json file.
            with open(__dot_secrets, "r") as file:
                dot_secrets = json.load(file)
                dot_secrets_formatted = json.dumps(dot_secrets, indent=4)
        except Exception as e:
            print(f"Decryption failed:{e}")
            exit(1)

    print("Decryption successful.")
else:
    print("Data was already decrypted.")

access_keys: DataFrame = __load_csv(__access_keys, "Secret")
"""CSV Access keys for... who knows."""
credentials: DataFrame = __load_csv(__credentials, "Password")
"""CSV Credentials for... :)."""

if flag_secrets:
    print(f"Hiding secret data from the terminal will also censor the {LE_SECRETS}!")
else:
    print(
        f".secrets:\n{dot_secrets_formatted}\n\n"
        f"access_keys:\n{access_keys}\n\n"
        f"credentials:\n{credentials}"
    )

unsecure: str = dot_secrets["unsecure"]
rds_secrets: Dict[str, str] = dot_secrets["RDS"]
s3_secrets: Dict[str, str] = dot_secrets["S3"]
dynamo_secret: str = dot_secrets["DynamoDB"]

print("[clownkey end]\n\n\n")
