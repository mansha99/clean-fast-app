# Prerequisites
- python installed
- uv installed
- postgresql installed
- database `contact_db` created
- table `contacts` is created inside `contact_db` database
## SQL Script to create table
```sql
-- DB name : contact_db
CREATE TABLE contacts (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    mobile VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(50) NOT NULL
);
```
# How to run
- clone repository
- cd <repository>
```shell 
uv sync
uv run uvicorn interface.api.main:app --app-dir src --reload --port 8000
```
Now open `http://127.0.0.1:8000/docs` and test following endpoints
- POST    /api/v1/contacts      to create a new contact 
- POST   /api/v1/contacts       to list all the contacts

# Optional
ruff check          analyze code to find bugs, style errors, and code quality issues
ruff check --fix    analyze and fix
