import os
import psycopg2
from dotenv import load_dotenv  # Securely load credentials
import pandas as pd

# Load environment variables
load_dotenv()

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )

    # Read data into Pandas DataFrame
    query = "SELECT * FROM jobs;"
    df = pd.read_sql_query(query, conn)  

    # Save to CSV
    df.to_csv("exported_jobs.csv", index=False)
    print("Export completed successfully!")

except psycopg2.Error as e:
    print(f"Database error: {e}")

finally:
    # Close connection safely
    if 'conn' in locals() and conn is not None:
        conn.close()
        print("Connection closed.")
