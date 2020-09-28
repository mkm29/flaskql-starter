from graphene import ObjectType, Field, ResolveInfo, List
from app.connections import Project, User
from app.utils import input_to_dictionary
from app.types import ProjectUserType
from sqlalchemy.sql import text
from app import attributes
from datetime import datetime
from sqlalchemy import func
from typing import List as ListType, Type, Dict, Union, Set, Any, Tuple, Optional


class Query(ObjectType):
    get_projects = Field(lambda: List(Project), data=attributes.ProjectInput())
    get_user = Field(lambda: User, data=attributes.UserInput())
    get_project_users = Field(
        lambda: ProjectUserType, data=attributes.ProjectUsersInput(required=True)
    )

    def resolve_get_projects(
        self: Type[ObjectType],
        info: Type[ResolveInfo],
        data: Optional[Type[attributes.ProjectUsersInput]] = None,
    ) -> Type[ListType[Project]]:
        query = Project.get_query(info)
        if data:
            data = input_to_dictionary(data)
            for key, value in data.items():
                query = query.filter(text(f"{key}='{value}'"))
        return query.all()

    def resolve_get_user(
        self: Type[ObjectType],
        info: Type[ResolveInfo],
        data: Type[attributes.UserInput],
    ) -> Type[ListType[User]]:
        query = User.get_query(info)
        data = input_to_dictionary(data)
        for key, value in data.items():
            query = query.filter(text(f"{key}='{value}'"))
        return query.first()

    def resolve_get_project_users(
        self: Type[ObjectType],
        info: Type[ResolveInfo],
        data: Type[attributes.ProjectUsersInput],
    ) -> Type[ListType[ProjectUserType]]:
        data = input_to_dictionary(data)
        # Get Project Attributes
        project_attrs = ['project_id', 'name', 'hours']
        project_query = Project.get_query(info)
        for key, value in data.items()[project_attrs]:
            project_query = project_query.filter(text(f"{key}='{value}'"))
        project = project_query.first()

        user_attrs = ['user_id', 'first_name', 'last_name', 'email']
        user_query = User.get_query(info)
        for key, value in data.items()[user_attrs]:
            user_query = user_query.filter(text(f"{key}='{value}'"))
        users = user_query.all()

        # Combine the 2
        project_users = ProjectUserType(project=project, users=users)
        return project_users

