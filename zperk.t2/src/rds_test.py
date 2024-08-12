__all__ = ["rds_endpoint", "rds_username", "rds_password"]

import sys
import os
from typing import Any
import mysql.connector

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.secrets"))
)

from clownkey import rds_secrets  # type:ignore

# Type hints.
rds: Any = rds_secrets

# Your AWS RDS instance details
rds_endpoint: str = rds["endpoint"]  # type: ignore
rds_username: str = rds["username"]  # type: ignore
rds_password: str = rds["password"]  # type: ignore

print("Testing AWS connection.")
try:
    # Connect to the RDS instance
    cnx = mysql.connector.connect(
        host=rds_endpoint,
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
