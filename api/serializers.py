from rest_framework import serializers
from app.models import Tutorial, Tag

class TutorialSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Tutorial
        fields = ('__all__')

class TutorialPOST(serializers.Serializer):
    """post a tutorial through the API"""

    class Meta:
        model = Tutorial
        fields = ('link', 'category')

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('__all__')
