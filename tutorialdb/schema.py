import graphene
import app.schema 
from graphene_django.debug import DjangoDebug  #type:ignore


class Query(app.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(app.schema.Mutation, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query, mutation=Mutation)

