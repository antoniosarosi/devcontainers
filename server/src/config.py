import os

from dotenv import load_dotenv


load_dotenv()


def build_database_uri() -> str:
    host = os.environ["DB_HOST"]
    port = os.environ["DB_PORT"]
    database = os.environ["DB_DATABASE"]
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]

    return f"mysql://{user}:{password}@{host}:{port}/{database}"


DATABASE_URI = build_database_uri()
