-- Run as postgres superuser once after installing postgresql-16-pgvector.
-- This file is a reference; the alembic migration also issues CREATE EXTENSION IF NOT EXISTS.

-- Create the role and database (skip if already present)
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'prufrock') THEN
    CREATE ROLE prufrock LOGIN PASSWORD 'CHANGE_ME';
  END IF;
END
$$;

CREATE DATABASE prufrock OWNER prufrock;

\c prufrock

-- Enable pgvector (unused in experiment 0; reserved for line-similarity in later experiments)
CREATE EXTENSION IF NOT EXISTS vector;

-- Grant all on future tables to the prufrock role (alembic creates as superuser)
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO prufrock;
