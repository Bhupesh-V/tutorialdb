import graphene
from graphene_django.types import DjangoObjectType

from .models import Tag



class TagType(DjangoObjectType):
    class Meta:
        model = Tag

class Query(object):
     all_tags = graphene.List(TagType)
     def resolve_all_tags(self, info, **kwargs):
      	 return Tag.objects.all() 

    
