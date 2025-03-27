import pytest
import pandas as pd
import psycopg2
from remote_jobs.export_to_csv import export_to_csv

@pytest.fixture
def mock_db_connection(monkeypatch):
    """Mock PostgreSQL database connection"""

    class MockCursor:
        def execute(self, query, params=None):
            # Simulate query execution (do nothing)
            pass
        
        def fetchall(self):
            # Return mock data for the SELECT query
            return [
                (1, "Software Engineer", "Tech Corp", "Remote", "https://weworkremotely.com/jobs/123-job")
            ]
        
        @property
        def description(self):
            # Return mock column names for SELECT query
            return [("id",), ("title",), ("company",), ("location",), ("link",)]
        
        def close(self):
            pass

    class MockConnection:
        def cursor(self):
            # Return the mock cursor when cursor() is called
            return MockCursor()
        
        def commit(self):
            pass
        
        def close(self):
            pass

    # Monkeypatch psycopg2.connect to return the MockConnection instance
    monkeypatch.setattr(psycopg2, "connect", lambda *args, **kwargs: MockConnection())

@pytest.mark.usefixtures("mock_db_connection")
def test_export_to_csv(tmp_path):
    """Test export_to_csv function by verifying CSV output"""

    output_file = tmp_path / "test_jobs.csv"

    # Run the export function
    try:
        export_to_csv(output_path=str(output_file))
    except Exception as e:
        pytest.fail(f"export_to_csv() raised an exception: {e}")

    # Read and validate the CSV output
    df = pd.read_csv(output_file)

    # Validate the contents of the CSV
    assert len(df) == 1
    assert df.iloc[0]["title"] == "Software Engineer"
    assert df.iloc[0]["company"] == "Tech Corp"
    assert df.iloc[0]["location"] == "Remote"
    assert df.iloc[0]["link"] == "https://weworkremotely.com/jobs/123-job"
