# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import psycopg2
from dotenv import load_dotenv  # Securely load credentials
from scrapy.exceptions import DropItem

class PostgresPipeline:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file

        self.connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
        self.cursor = self.connection.cursor()

        # Ensure the table exists
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                location TEXT NOT NULL,
                link TEXT UNIQUE NOT NULL,
                employment_type TEXT DEFAULT 'Unknown',
                salary TEXT DEFAULT 'Not Specified'
            );
        """)
        self.connection.commit()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """
                INSERT INTO jobs (title, company, location, link, employment_type, salary) 
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (link) DO NOTHING
                """,
                (item["title"], item["company"], item["location"], item["link"], item["employment_type"], item["salary"])
            )
            self.connection.commit()
            spider.logger.info(f"Successfully saved: {item['title']} at {item['company']}")
        except psycopg2.Error as e:
            spider.logger.error(f"Database Error: {e} | Item: {item}")
            return item  # Continue processing next item

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()



class RemoteJobsPipeline:
    def process_item(self, item, spider):
        return item
