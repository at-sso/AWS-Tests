__all__ = ["rds_host", "rds_username", "rds_password"]

import sys
import os
from typing import Dict
import mysql.connector

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.secrets"))
)

from clownkey import dot_secrets

# Type hint.
secrets: Dict[str, str] = dot_secrets.get("RDS")

# Your AWS RDS instance details
rds_host: str = secrets.get("endpoint")  # type: ignore
rds_username: str = secrets.get("username")  # type: ignore
rds_password: str = secrets.get("password")  # type: ignore

print("Testing AWS connection.")
try:
    # Connect to the RDS instance
    cnx = mysql.connector.connect(
        host=rds_host,
        port=3306,
        user=rds_username,
        password=rds_password,
    )

    cursor = cnx.cursor()
    cursor.execute("SELECT DATABASE()")
    cursor.fetchone()
    print("Success.")

    cursor.close()
    cnx.close()
except mysql.connector.Error as e:
    print(e)
    raise ConnectionError("Connection to Amazon RDS was not possible.")
