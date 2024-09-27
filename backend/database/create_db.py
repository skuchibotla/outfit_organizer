from dotenv import dotenv_values
import psycopg2

# Load environment variables
config = dotenv_values(".env")

try:
  # Connect to PostgreSQL db 
  psql_conn = psycopg2.connect(
    dbname=config['DB_NAME'],
    user=config['DB_USERNAME'],
    password=config['DB_PASSWORD'],
    host=config['DB_HOST'],
    port=config['DB_PORT']
  )

  psql_conn.autocommit = True

  cursor = psql_conn.cursor()

  # Execute SQL commands from the schema file
  with open('./database/schema.sql', 'r') as file:
    sql_queries = file.read()

  cursor.execute(sql_queries)
except Exception as e:
  print(f"An unexpected error has occured: {e}")
finally:
  if cursor:
    cursor.close()
  if psql_conn:
    psql_conn.close()
