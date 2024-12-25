from sqlalchemy import create_engine
from sqlalchemy import text
from dotenv import load_dotenv
import os


# loads .env file
load_dotenv()

# fetch variable form .env 
user = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')
driver = "mysql+pymysql"
port = 3306



# Create the connection string
connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

# Create engine and connect
engine = create_engine(connection_string)


# functin to fetch data from database
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM jobs'))
        jobs = []
        for row in result.all():
            jobs.append(row._mapping)
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text('select * from jobs where id = :val'),parameters={'val': id})
        row = result.first()
        if row is None:
            return None
        return {key: value for key, value in row._mapping.items()}
