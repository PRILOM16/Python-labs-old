import sqlite3
import os
from typing import Any


def insert_data_into_tables(
    db_path: str, data_by_tables: dict[str, list[list[Any]]]
) -> None:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for table_name, rows in data_by_tables.items():
        for row in rows:
            placeholders = ", ".join(["?"] * len(row))
            query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(query, row)

    conn.commit()
    conn.close()


def main() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    db_file = os.path.join(script_dir, "library.db")

    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Author (id INTEGER PRIMARY KEY, name TEXT)"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Book (id INTEGER PRIMARY KEY, title TEXT, author_id INTEGER)"
    )
    conn.commit()
    conn.close()

    data_to_insert = {
        "Author": [
            [1, "Лев Толстой"],
            [2, "Федор Достоевский"],
        ],
        "Book": [
            [1, "Война и мир", 1],
            [2, "Преступление и наказание", 2],
        ],
    }

    insert_data_into_tables(db_file, data_to_insert)

    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Author")
    print("Данные в таблице Author:", cur.fetchall())

    cur.execute("SELECT * FROM Book")
    print("Данные в таблице Book:", cur.fetchall())
    conn.close()


if __name__ == "__main__":
    main()