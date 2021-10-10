-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

CREATE SCHEMA whodat;
-- DROP TABLE IF EXISTS public.processing_tasks;

-- Table Definition
CREATE TABLE whodat.target
(
    id SERIAL PRIMARY KEY,
    json_doc JSONB NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

INSERT INTO whodat.target (json_doc) VALUES
('{"toto":"titi"}'::JSONB);