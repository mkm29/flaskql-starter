# """ Create Flask app """

# from flask import Flask
# from flask_graphql import GraphQLView
# from flask_cors import CORS
# from healthcheck import HealthCheck


# def create_app(env=None):

#     # initialize app
#     app = Flask(__name__)
#     CORS(app)
#     app.debug = True

#     app.add_url_rule(
#         "/", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
#     )

#     # Initialize Health Check
#     # need to setup a health path in OpenShift
#     health = HealthCheck(app, "/health")

#     return app
