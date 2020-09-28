import graphene
from app.queries import Query
from app.mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
