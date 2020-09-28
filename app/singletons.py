import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


""" Database configuration """


def config():
    return "sqlite:///projects.db"


connection_string = config()
# print(connection_string)
ENGINE = create_engine(connection_string, convert_unicode=True)

DB_SESSION = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
)

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
