---

# Remote Jobs Scraper

A web scraping pipeline built with **Scrapy** to extract remote programming job listings from **We Work Remotely**. Data is dynamically scraped, routed through a custom pipeline into a **PostgreSQL** database with built-in deduplication, and can be exported cleanly to a CSV file via a utility **Pandas** script.

## 🚀 Key Features

* **Targeted Extraction:** Built specifically to parse the *Remote Programming Jobs* category on We Work Remotely.
* **Granular Data Points:** Captures job title, company, headquarters location, source link, employment type (Full-Time/Part-Time), and salary strings.
* **Automated Table Initialization:** The database pipeline uses `CREATE TABLE IF NOT EXISTS` to automatically spin up your schema on its first run.
* **Safe Ingestion & Deduplication:** Uses PostgreSQL `ON CONFLICT (link) DO NOTHING` constraints to prevent database duplication on repeated runs.
* **Secure Configurations:** Uses `python-dotenv` to safeguard database credentials.
* **Pandas Data Export:** Includes a dedicated standalone script to pull database rows into a structured Pandas DataFrame and output a clean CSV.
* **Test-Driven:** Fully integrated with `pytest` for validation.

---

## ⚙️ 1. Installation & Setup

### Prerequisites

* **Python 3.8+**
* **PostgreSQL** instance running locally or remotely

### Setup Steps

1. **Clone the Repository:**
```bash
git clone https://github.com/Mbulelo-Peyi/remote_jobs-scraper.git
cd remote_jobs-scraper

```


2. **Set Up a Virtual Environment:**
* **macOS/Linux:**
```bash
python -m venv venv && source venv/bin/activate

```


* **Windows:**
```bash
python -m venv venv && .\venv\Scripts\activate

```




3. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


*(Ensure your `requirements.txt` contains `scrapy`, `scrapy-playwright`, `psycopg2` or `psycopg2-binary`, `pandas`, `python-dotenv`, and `pytest`)*
4. **Install Playwright Browsers:**
Initialize the underlying headless Chromium binary configured in your settings:
```bash
playwright install chromium

```



---

## 🗄️ 2. Environment Configuration

### Step 1: Create the Database Shell

Log into your PostgreSQL client (pgAdmin, psql, etc.) and create an empty database:

```sql
CREATE DATABASE scraper_db;

```

> 💡 **Note:** You do not need to create tables or columns manually. The pipeline script generates them automatically when you launch the spider.

### Step 2: Configure Environment Variables

Create a file named `.env` in the root directory of your project and populate it with your database connection parameters:

```text
DB_NAME=scraper_db
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
DB_HOST=127.0.0.1
DB_PORT=5432

```

---

## 💻 3. Usage & Execution

### Running the Scraper

Execute the spider to crawl listings and populate your database:

```bash
scrapy crawl weworkremotely

```

*Alternative module invocation syntax:*

```bash
python -m scrapy crawl weworkremotely

```

### Exporting Data to CSV

Run the standalone script to dump all scraped jobs from the database into a `exported_jobs.csv` file using Pandas:

```bash
python export_to_csv.py

```

---

## 📊 Data Schema Definition

The database pipeline will automatically spin up a table named `jobs` with the following configuration:

| Column Name | Data Type | Constraints / Defaults |
| --- | --- | --- |
| `id` | `SERIAL` | `PRIMARY KEY` |
| `title` | `TEXT` | `NOT NULL` |
| `company` | `TEXT` | `NOT NULL` |
| `location` | `TEXT` | `NOT NULL` |
| `link` | `TEXT` | `UNIQUE NOT NULL` |
| `employment_type` | `TEXT` | `DEFAULT 'Unknown'` |
| `salary` | `TEXT` | `DEFAULT 'Not Specified'` |

---

## 🧪 4. Testing Suite

Run your `pytest` suite to verify extraction selectors, pipeline logic, and database commits:

```bash
# General test run
pytest

# Verbose testing mode
pytest -v

```

---

## 🤝 5. Contributing

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 6. License

Distributed under the MIT License. See `LICENSE` for details.
