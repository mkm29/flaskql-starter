""" Customn return types for GraphQL """

from graphene import ObjectType, Int, Field, List, Boolean, String
from graphene.types import DateTime
from app.connections import Project, User


class ProjectUserType(ObjectType):
    """ Graphene Type for combining Project and User models """

    project = Field(lambda: Project)
    users = Field(lambda: List(User))
