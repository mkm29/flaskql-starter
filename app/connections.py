""" Map SQLAlchemy models to Graph objects """

from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyObjectType
from graphene import relay
from app.singletons import DB_SESSION, ENGINE
from app import models


class User(SQLAlchemyObjectType):
    """ SQLAlchemy Object Type for User """

    class Meta:
        """ Meta Class to map a SQLAlchemy model to GraphQL """

        model = models.User
        interface = (relay.Node,)


class UserConnection(relay.Connection):
    class Meta:
        node = User


class Project(SQLAlchemyObjectType):
    """ SQLAlchemy Object Type for Project """

    class Meta:
        """ Meta Class to map a SQLAlchemy model to GraphQL """

        model = models.Project
        interface = (relay.Node,)


class PropjectConnection(relay.Connection):
    """ Graphene Connection Object for Project """

    class Meta:
        """ Standard Meta Class for Graphene Connections """

        node = Project
