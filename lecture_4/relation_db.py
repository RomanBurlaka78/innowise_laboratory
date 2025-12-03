import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()
sql_script = ""

def read_sql_file():
    #1. Read SQL commands from the file
    global sql_script
    try:
        with open("a.sql", "r") as file:
            sql_script = file.read()
    except FileNotFoundError:
        print("Error: 'a.sql' file not found.")
        sql_script = ""


def execute_sql_scripts():
    # Execute the SQL script
    if not sql_script.strip():
        print("No SQL script to execute.")
        return
    try:
        cur.executescript(sql_script)

    except Exception as e:
        print(f"SQL execution error: {e}")



def save_change_close():
    # Save changes and close
    try:
        con.commit()
        print("Database 'school.db' created with sample data.")
    except Exception as e:
        print(f"Commit error: {e}")
    finally:
        con.close()
        print("Database 'school.db' closed.")



def main():
    read_sql_file()
    execute_sql_scripts()
    save_change_close()


if __name__ == "__main__":
    main()
