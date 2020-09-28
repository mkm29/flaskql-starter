import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


""" Database configuration """


def config():
    return "sqlite:///projects.db"
    # If using Postgres, set local ENV vars in .envrc file
    port = os.environ.get("POSTGRESQL_SERVICE_PORT")
    host = os.environ.get("POSTGRESQL_SERVICE_HOST")
    user = os.environ.get("POSTGRESQL_USER")
    database = os.environ.get("POSTGRES_DB")
    password = os.environ.get("POSTGRES_PASSWORD")
    return f"postgresql://{user}:{password}@{host}:{port}/{database}"


connection_string = config()
# print(connection_string)
ENGINE = create_engine(connection_string, convert_unicode=True)

DB_SESSION = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
)

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
