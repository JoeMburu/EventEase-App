import psycopg2
from psycopg2 import sql
from urllib.parse import urlparse

# Database URL
DATABASE_URL = "postgresql://neondb_owner:zNBQYHMUF64j@ep-quiet-bread-a2bmbfh6.eu-central-1.aws.neon.tech/zero_user_gains_955285"

def delete_and_recreate_database(database_url):
    # Parse the database URL
    parsed_url = urlparse(database_url)
    username = parsed_url.username
    password = parsed_url.password
    hostname = parsed_url.hostname
    port = parsed_url.port
    database_name = parsed_url.path.lstrip('/')  # Remove leading slash

    try:
        # Connect to the PostgreSQL server using the admin database (default: 'postgres')
        connection = psycopg2.connect(
            dbname="postgres",  # Admin database
            user=username,
            password=password,
            host=hostname,
            port=port
        )
        connection.autocommit = True  # Enable autocommit for DDL operations
        cursor = connection.cursor()

        # Drop the target database
        print(f"Deleting database '{database_name}'...")
        cursor.execute(sql.SQL("DROP DATABASE IF EXISTS {}").format(sql.Identifier(database_name)))
        print(f"Database '{database_name}' deleted successfully.")

        # Recreate the target database
        print(f"Recreating database '{database_name}'...")
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database_name)))
        print(f"Database '{database_name}' created successfully.")

        # Close the connection
        cursor.close()
        connection.close()

    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    delete_and_recreate_database(DATABASE_URL)
