import subprocess
import json
import os
import platform
import pandas as pd
from pandas import DataFrame
from getpass import getpass as gp

from flags import *
from var import *

# Installs Gpg4win on Windows if not already installed.
if platform.system() == "Windows" and not flag_win:
    print("Trying to install 'Gpg4win'. This tool is needed to decrypt the files.")
    subprocess.run("winget install --id GnuPG.Gpg4win")


print("This Path ->", this_path)
print("Easter Eggs ->", easter_egg)

try:
    # Ensure the download directory exists
    os.mkdir(os.path.join(f"{this_path}/env", f"{this_path}/env/download"))
except:  # The directory does exist. I don't know why they raise an exception in this case like wtf dude, not cool.
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


# Try to load the '.secrets' file if it exists
try:
    with open(dot_secrets_path, "r") as file:
        dot_secrets = json.load(file)
except FileNotFoundError:  # The file wasn't encrypted yet.
    pass
finally:
    dot_secrets_formatted = json.dumps(dot_secrets, indent=4) if dot_secrets else ""


# If the required files don't already exist, start the operation
if not __files_exist() and not flag_skip_decrypt:
    # Helper flag to identify if user input is needed to complete the operation
    input_passphrase: bool = False

    # If the decrypt flag was set, set the path variables.
    if flag_decrypt:
        try:
            dot_secrets_path = __decrypt(flag_decrypt[0], ".secrets")
            access_keys_path = __decrypt(flag_decrypt[1], "accessKeys.gpg", True)
            credentials_path = __decrypt(flag_decrypt[2], "credentials.gpg", True)
        except Exception as e:
            print(f"An error occurred:{e}\nTrying to get passphrases from user input.")
            input_passphrase = True
    else:
        input_passphrase = True

    # Either an error occurred or `flag_decrypt` was not set.
    if input_passphrase:
        try:
            print("Note: `getpass` function is being used. Input IS being received.")
            dot_secrets_path = __decrypt(gp(".secrets: "), ".secrets")
            access_keys_path = __decrypt(gp("accessKeys: "), "accessKeys.gpg", True)
            credentials_path = __decrypt(gp("credentials: "), "credentials.gpg", True)
            # Once everything is set, get the decrypted json file.
            with open(dot_secrets_path, "r") as file:
                dot_secrets = json.load(file)
                dot_secrets_formatted = json.dumps(dot_secrets, indent=4)
        except Exception as e:
            print(f"Decryption failed:{e}")
            exit(1)

    print("Decryption successful.")
else:
    print("Data was already decrypted.")

access_keys: DataFrame = __load_csv(access_keys_path, "Secret")
"""CSV Access keys for AWS CLI. It must contain 'ID' and 'Secret' keys."""
credentials: DataFrame = __load_csv(credentials_path, "Password")
"""CSV Credentials for AWS CLI. it must contain 'User', 'Password', and 'Console' keys."""

if flag_secrets:
    print(f"Hiding secret data from the terminal will also censor the {LE_SECRETS}!")
else:
    print(
        f".secrets:\n{dot_secrets_formatted}\n\n"
        f"access_keys:\n{access_keys}\n\n"
        f"credentials:\n{credentials}"
    )


unsecure = dot_secrets["unsecure"]
rds_secrets = dot_secrets["RDS"]
s3_secrets = dot_secrets["S3"]
dynamo_secret = dot_secrets["DynamoDB"]
lambda_secrets = dot_secrets["Lambda"]
lambda_id = lambda_secrets["id"]
lambda_role = lambda_secrets["role"]
lambda_arn = lambda_secrets["arn"]

print("[clownkey end]\n\n\n")
