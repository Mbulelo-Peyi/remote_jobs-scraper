CREATE TABLE IF NOT EXISTS jobs (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    location TEXT NOT NULL,
    link TEXT UNIQUE NOT NULL,
    employment_type TEXT DEFAULT 'Unknown',
    salary TEXT DEFAULT 'Not Specified'
);