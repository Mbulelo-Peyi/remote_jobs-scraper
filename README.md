Remote Jobs Scraper
A web scraper for collecting remote job listings from We Work Remotely using Scrapy and storing the data in PostgreSQL. The scraper supports automated exports to CSV.

Features
✅ Scrapes job listings from We Work Remotely
✅ Stores data in PostgreSQL
✅ Exports job listings to CSV
✅ Supports Bright Data proxies (optional)
✅ Automated cron job scheduling

1. Installation & Setup
Prerequisites
Python 3.8+

PostgreSQL (with pgAdmin for management)

pip (Python package manager)

Clone the Repository
bash
Copy
Edit
git clone https://github.com/Mbulelo-Peyi/remote_jobs-scraper.git
cd remote_jobs-scraper
Create a Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
2. Database Setup
Create PostgreSQL Database
1️⃣ Start PostgreSQL and open psql or pgAdmin.
2️⃣ Run:

sql
Copy
Edit
CREATE DATABASE scraper_db;
3️⃣ Create a table for storing jobs:

sql
Copy
Edit
CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    location TEXT,
    link TEXT UNIQUE
);
4️⃣ Update PostgreSQL credentials in pipelines.py:

python
Copy
Edit
self.connection = psycopg2.connect(
    dbname="scraper_db",
    user="your_user",
    password="your_password",
    host="localhost",
    port="5432"
)
3. Running the Scraper
Start Scraping Jobs
bash
Copy
Edit
scrapy crawl weworkremotely
If you get a ModuleNotFoundError, try:

bash
Copy
Edit
python -m scrapy crawl weworkremotely
Verify Data in PostgreSQL
Run:

sql
Copy
Edit
SELECT * FROM jobs;
4. Export Data to CSV
bash
Copy
Edit
python export_to_csv.py
This will create exported_jobs.csv in the project directory.

5. Automate Scraping with Cron Jobs
Linux/macOS
Edit crontab:

bash
Copy
Edit
crontab -e
Run Scrapy every day at 2 AM:

bash
Copy
Edit
0 2 * * * cd /path/to/project && scrapy crawl weworkremotely >> logs.txt 2>&1
Export jobs to CSV at 2:30 AM:

bash
Copy
Edit
30 2 * * * cd /path/to/project && python export_to_csv.py
Windows (Task Scheduler)
1️⃣ Open Task Scheduler
2️⃣ Create a new task
3️⃣ Set trigger to daily at 2 AM
4️⃣ Action → Run Python script

Program: cmd.exe

Arguments:

bash
Copy
Edit
/c cd C:\path\to\project && scrapy crawl weworkremotely
5️⃣ Repeat for export script at 2:30 AM.

6. Running Tests
Run all tests:

bash
Copy
Edit
pytest tests/
For detailed output:

bash
Copy
Edit
pytest -v
7. CI/CD with GitHub Actions (Optional)
We will add this next! 🚀

8. Contributing
Report issues via GitHub Issues.

Feel free to fork and improve the project!

9. License
📜 MIT License

