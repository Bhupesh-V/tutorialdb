import graphene
from graphene_django.types import DjangoObjectType

from .models import Tag,Tutorial

class TagType(DjangoObjectType):
    class Meta:
        model = Tag

class TutorialType(DjangoObjectType):
    class Meta:
        model = Tutorial

class Query(object):
    tag = graphene.Field(TagType,
 			id = graphene.Int(),
			name = graphene.String())	
    all_tags = graphene.List(TagType)

    tutorial = graphene.Field(TutorialType,
			id = graphene.Int(),
			name = graphene.String())

    all_tutorials = graphene.List(TutorialType)

    def resolve_all_tags(self, info, **kwargs):
      	return Tag.objects.all() 

    def resolve_all_tutorials(self, info, **kwargs):
       	return Tutorial.objects.all()	

    def resolve_tag(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
	
        if id is not None:
	        return Tag.objects.get(pk=id)
        if name is not None:
	        return Tag.objects.get(name=name)	
        return None

