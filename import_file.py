import sqlite3

def import_file_paths(text_file, db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Read file paths from the text file
    with open(text_file, 'r') as file:
        file_paths = file.readlines()

    # Insert each file path into the database
    for path in file_paths:
        path = path.strip()  # Remove any leading/trailing whitespace
        try:
            cursor.execute('INSERT INTO tbfiles (filepath) VALUES (?)', (path,))
        except sqlite3.IntegrityError:
            print(f"File path already exists in the database: {path}")
        except Exception as e:
            print(f"Error inserting file path {path}: {e}")

    conn.commit()
    conn.close()

# Path to your text file and SQLite database
text_file_path = 'E:\\Data\\Medias\\allfiles.txt'
database_path = 'Music_Database.db'

# Import the file paths into the database
import_file_paths(text_file_path, database_path)
