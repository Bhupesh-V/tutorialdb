from rest_framework import serializers
from app.models import tutorial, tag

class tagSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = tag
		fields = ('__all__')

class tutorialSerializer(serializers.ModelSerializer):
	tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
	
	class Meta:
		model = tutorial
		fields = ('__all__')

class tutorialPOST(serializers.Serializer):

	class Meta:
		model = tutorial
		fields = ('link', 'category')