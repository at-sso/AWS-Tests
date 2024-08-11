import sys
import os
from typing import Dict
import mysql.connector

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.secrets"))
)

from clownkey import dot_secrets  # type: ignore

# Type hint.
secrets: Dict[str, str] = dot_secrets.get("RDS")  # type: ignore

# Your AWS RDS instance details
host: str = secrets.get("endpoint")  # type: ignore
username: str = secrets.get("username")  # type: ignore
password: str = secrets.get("password")  # type: ignore

print("Testing AWS connection.")
try:
    # Connect to the RDS instance
    cnx = mysql.connector.connect(
        host=host,
        port=3306,
        user=username,
        password=password,
    )

    cursor = cnx.cursor()
    cursor.execute("SELECT DATABASE()")
    print(cursor.fetchone(), "\nSuccess.")

    cursor.close()
    cnx.close()
except mysql.connector.Error as e:
    print(e)
