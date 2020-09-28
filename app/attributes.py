from graphene import InputObjectType, Int, String
from graphene.types.datetime import DateTime, Date


class ProjectInput(InputObjectType):
    """ Arguments to create or query Projects """

    project_id = Int()
    name = String()
    hours = Int()


class UserInput(InputObjectType):
    user_id = Int()
    first_name = String()
    last_name = String()
    email = String()


class ProjectUsersInput(ProjectInput, UserInput):
    pass
