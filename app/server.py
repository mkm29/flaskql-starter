from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS
from healthcheck import HealthCheck
from app.singletons import DB_SESSION, ENGINE
from app.models import Base
from graphene import Schema
from app.queries import Query
from app.mutations import Mutation
from graphene import Schema


def create_app(env=None):

    # initialize app
    app = Flask(__name__)
    CORS(app)
    app.debug = True

    Base.metadata.create_all(ENGINE)

    schema = Schema(query=Query, mutation=Mutation)

    app.add_url_rule(
        "/", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
    )

    # Initialize Health Check
    # need to setup a health path in OpenShift
    HealthCheck(app, "/health")

    return app
