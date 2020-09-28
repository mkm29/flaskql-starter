from graphene import Mutation, List, Field, ObjectType, Int, Boolean
from app import models
from app import connections
from app import attributes
from app.utils import input_to_dictionary
from app.authentication import authenticate
from app.exceptions import DatabaseTransactionException
from app.singletons import DB_SESSION
from sqlalchemy.exc import SQLAlchemyError


class CreateProject(Mutation):
    project = Field(lambda: connections.Project)
    status = Boolean()

    class Arguments:
        data = attributes.ProjectInput()
        data.name.required = True
        data.hours.required = True

    # @authenticate(endpoint="create_project")
    def mutate(self, info, data):
        data = input_to_dictionary(data)
        data.pop("project_id", None)
        project = models.Project(**data)
        try:
            DB_SESSION.add(project)
            DB_SESSION.commit()
        except SQLAlchemyError as e:
            DB_SESSION.rollback()
            raise DatabaseTransactionException(args=e.args, message=e._message)
        return CreateProject(project=project)

# class UpdateProject(Mutation):
#     project = Field(lambda: connections.Project)

#     class Arguments:
#         data = attributes.ProjectInput(required=True)
#         data.project_id.required = True

#     def mutate(self, info, data):



class Mutation(ObjectType):
    create_project = CreateProject.Field()
