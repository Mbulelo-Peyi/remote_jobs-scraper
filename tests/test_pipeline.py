import pytest
import psycopg2
from unittest import mock
from remote_jobs.pipelines import PostgresPipeline

@pytest.fixture
def pipeline(mocker):  # Patch psycopg2.connect before instantiating the pipeline
    mock_conn = mocker.patch("psycopg2.connect", autospec=True)
    mock_cursor = mock_conn.return_value.cursor.return_value

    pipeline = PostgresPipeline()  # Now uses the mocked connection
    return pipeline, mock_cursor  # Return both for test access

def test_pipeline_inserts_data(pipeline):
    pipeline_instance, mock_cursor = pipeline  # Unpack the fixture

    # Item to be inserted into the database
    item = {
        "title": "Software Engineer",
        "company": "Tech Corp",
        "location": "Remote",
        "link": "https://weworkremotely.com/jobs/123-job",
        "employment_type": "Full-Time",
        "salary": "$100,000"
    }

    # Call the process_item method
    pipeline_instance.process_item(item, spider=None)

    # Normalize SQL query to avoid whitespace issues
    expected_query = """
        INSERT INTO jobs (title, company, location, link, employment_type, salary)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (link) DO NOTHING
    """.strip()

    # Get the actual SQL query executed
    actual_query = mock_cursor.execute.call_args[0][0].strip()
    actual_params = mock_cursor.execute.call
