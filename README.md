# Remote Jobs Scraper  
A web scraper for collecting remote job listings from We Work Remotely using Scrapy and storing the data in PostgreSQL. The scraper supports automated exports to CSV.  

## Features  
✅ Scrapes job listings from We Work Remotely  
✅ Stores data in PostgreSQL  
✅ Exports job listings to CSV  
✅ Supports Bright Data proxies (optional)  
✅ Automated cron job scheduling  

## 1. Installation & Setup  
### Prerequisites  
- Python 3.8+  
- PostgreSQL (with pgAdmin for management)  
- pip (Python package manager)  

### Steps  
1. Clone the Repository:  
`git clone https://github.com/Mbulelo-Peyi/remote_jobs-scraper.git` then `cd remote_jobs-scraper`  

2. Create and activate Virtual Environment:  
`python -m venv venv` then `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows)  

3. Install Dependencies:  
`pip install -r requirements.txt`  

## 2. Database Setup  
### Steps  
1. Create PostgreSQL Database:  
Run `CREATE DATABASE scraper_db;` in your PostgreSQL client  

2. Create Jobs Table:  
Run: `CREATE TABLE jobs (id SERIAL PRIMARY KEY, title TEXT NOT NULL, company TEXT NOT NULL, location TEXT, link TEXT UNIQUE);`  

3. Update credentials in pipelines.py with your database details  

## 3. Running the Scraper  
### Steps  
1. Start Scraping:  
`scrapy crawl weworkremotely` or if error `python -m scrapy crawl weworkremotely`  

2. Verify Data:  
Check PostgreSQL with: `SELECT * FROM jobs;`  

## 4. Export Data to CSV  
Run: `python export_to_csv.py` (creates exported_jobs.csv)  

## 5. Automate with Cron Jobs  
### Linux/macOS  
1. Edit crontab: `crontab -e`  
2. Add:  
`0 2 * * * cd /path/to/project && scrapy crawl weworkremotely >> logs.txt 2>&1`  
`30 2 * * * cd /path/to/project && python export_to_csv.py`  

### Windows  
1. Create Task Scheduler task  
2. Set daily at 2 AM  
3. Action: Run cmd.exe with: `/c cd C:\path\to\project && scrapy crawl weworkremotely`  

## 6. Running Tests  
Run: `pytest tests/` or `pytest -v` for verbose output  

## 7. CI/CD  
Coming soon! 🚀  

## 8. Contributing  
Report issues via GitHub Issues. Fork and improve the project!  

## 9. License  
MIT License