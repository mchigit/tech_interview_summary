#Title (Undetermined)

This web app contains a summary of the algorithms and data structure that may appear in a technical interview,
including description, use cases and implementations. 

## Development Environment

This project is written in Python/Django framework, using PostgreSQL 10.3 as database. 

Make sure you install:
 - Python 3.6 (https://www.python.org/downloads/)
 - PostgreSQL 10.3 (https://www.postgresql.org/download/)

Make sure these are installed by opening command line and check:
- `python -V` : should return the version of your python
- `pip -V` : should return the current version of pip. (This is included if using Python 3.4 + )

To use PostgreSQL with Django, make sure you have **Psycopg2**:
- open command line and run `pip install -U psycopg2`

## Getting Started

Clone this repository and navigate to the project root

```bash
git clone git@github.com:michaelchi1997/tech_interview_summary.git
cd tech_interview_summary
```
To create the database schema, take a look at the `settings.py` under `project_root/tech_interview_summary`
and follow the configurations. 

After database and user are created, run migrations using following command:

```bash
python manage.py migrate
```

Run server:

```bash
python manage.py runserver localhost:8000
```

Navigate to  [http://localhost:8000/](http://localhost:8000/)
