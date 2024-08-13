import sys
import mysql.connector
from mysql.connector import errorcode
from typing import Callable, Dict, Any
from rds_test import *


def create_db(cursor: Any, conn: Any) -> None:
    # Create a table in the bookstore database
    create_table_query = """
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        price DECIMAL(5, 2) NOT NULL,
        published_date DATE
    )
    """
    cursor.execute(create_table_query)
    print("Table 'books' created.")

    # Insert sample data
    insert_data_query = """
    INSERT INTO books (title, author, price, published_date)
    VALUES
        ('The Catcher in the Rye', 'J.D. Salinger', 10.99, '1951-07-16'),
        ('To Kill a Mockingbird', 'Harper Lee', 7.99, '1960-07-11'),
        ('1984', 'George Orwell', 8.99, '1949-06-08')
    """
    cursor.execute(insert_data_query)
    conn.commit()
    print("Sample data inserted into 'books'.")


def show_db(cursor: Any) -> None:
    select_query = "SELECT * FROM books"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    print("\nBooks in the bookstore:")
    for row in rows:
        print(row)


def clear_db(cursor: Any, conn: Any) -> None:
    delete_query = "DELETE FROM books"
    cursor.execute(delete_query)
    conn.commit()
    print("All records deleted from 'books'.")

    drop_query = "DROP TABLE IF EXISTS books"
    cursor.execute(drop_query)
    conn.commit()
    print("Table 'books' dropped.")


def close_conn(cursor: Any, conn: Any) -> None:
    # Close the connection
    cursor.close()
    conn.close()
    print("\nDatabase connection closed.")


def main() -> int:
    # Connect to Amazon RDS
    try:
        conn = mysql.connector.connect(
            user=rds_username, password=rds_password, host=rds_endpoint
        )
        cursor = conn.cursor()
        print("Connected to the database.")
        # Set the database after successful connection
        conn.database = "bookstore"  # type: ignore[union-attr]
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password.")
            return 2
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist. Creating database.")
            conn = mysql.connector.connect(
                user=rds_username, password=rds_password, host=rds_endpoint
            )
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE bookstore")
            # Set the database after creation
            conn.database = "bookstore"  # type: ignore[union-attr]
        else:
            print(err)
            return 1

    execute: Dict[int, Callable[[Any, Any], None]] = {
        1: lambda cursor, conn: create_db(cursor, conn),
        2: lambda cursor, x: show_db(cursor),
        3: lambda cursor, conn: clear_db(cursor, conn),
    }

    print("1. Create database\n2. Check database\n3. Clear database\n0. Exit")
    while True:
        selector: str = input("> ")

        if selector == "0":
            break
        if selector not in ["1", "2", "3"]:
            print("Select a valid input.")
            continue
        try:
            execute[int(selector)](cursor, conn)
        except mysql.connector.ProgrammingError as err:
            print(err)
            continue
        except mysql.connector.Error as err:
            close_conn(cursor, conn)
            print(err)
            return 3

    close_conn(cursor, conn)
    return 0


friendly_code: Dict[int, str] = {
    0: "Success.",
    1: "Connection error.",
    2: "Bad credentials.",
    3: "Database error.",
    4: "Unhandled error.",
}

if __name__ == "__main__":
    try:
        a = main()
    except Exception as err:
        print(err)
        a = 4
    print(friendly_code[a])
    sys.exit(a)
