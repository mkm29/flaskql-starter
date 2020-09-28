""" Define database models """

from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.singletons import DB_SESSION


Base = declarative_base()
Base.query = DB_SESSION.query_property()


class User(Base):
    """ User model """

    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)


class Project(Base):
    """ Project model """

    __tablename__ = "project"
    project_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hours = Column(Integer)
    # TODO - users
    users = relationship("User", secondary=lambda: project_users, backref="project")


project_users = Table(
    "project_users",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("project.project_id"), primary_key=True),
    Column("user_id", String, ForeignKey("user.user_id"), primary_key=True),
)
