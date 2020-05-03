from  graphene_django.rest_framework.mutation import SerializerMutation
from api.serializers import TagSerializer, TutorialSerializer 


class TagMutation(SerializerMutation):
	class Meta:
		serializer_class = TagSerializer 
		model_operations = ['create', 'update']
		lookup_field = 'id'

