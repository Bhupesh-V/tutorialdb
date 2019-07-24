from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import tutorialSerializer, tagSerializer, tutorialPOST
from django.shortcuts import render
from app.models import tutorial, tag
from taggie.parser import generateTags

 
# Just wraps a simple HTTP Response to a JSON Response
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET'])
def index(request):
    return render(request, 'api.html')


@api_view(['GET'])
def tutorial_Tags(request, tags):
	"""
	Return tutorials with a {tag}
	"""
	tags = tags.split(',')
	customTutorials = tutorial.objects.filter(tags__name__in = tags).distinct()
	serializer = tutorialSerializer(customTutorials, many=True)
	return JSONResponse(serializer.data)

@api_view(['GET'])
def latest(request):
	"""
	Return latest 10 tutorials from tutorialdb
	"""
	results = tutorial.objects.all().order_by('-created_date')[:10]
	serializer = tutorialSerializer(results, many=True)
	return JSONResponse(serializer.data)


@api_view(['GET'])
def tutorial_Tags_Category(request, tags, category):
	"""
	Return tutorials with a {tag} and {category}
	"""
	tags = tags.split(',')
	category = category.split(',')
	customTutorials = tutorial.objects.filter(tags__name__in = tags, category__in = category).distinct()
	serializer = tutorialSerializer(customTutorials, many=True)
	return JSONResponse(serializer.data)


@api_view(['GET'])
def tags(request):
	"""
	Returns all tags

	"""
	tags = tag.objects.all()
	serializer = tagSerializer(tags, many=True)
	return JSONResponse(serializer.data)


@api_view(['GET', 'POST'])
def tutorials(request):
	"""
	get: Returns all tutorials

	post: POST a tutorial
	"""
	if request.method == 'GET':
		tutorials = tutorial.objects.all()
		serializer = tutorialSerializer(tutorials, many=True)
		return JSONResponse(serializer.data)
	elif request.method == 'POST':
		postserializer = tutorialPOST(data = request.data)
		if postserializer.is_valid():
			linkCount = tutorial.objects.filter(link = request.data['link']).count()
			if linkCount == 0:
				tags, title = generateTags(request.data['link'])
				if 'other' in tags:
					return JSONResponse({"message " : "Not a tutorial link" }, status=HTTP_406_NOT_ACCEPTABLE)
				else:
					tutorialObject = tutorial.objects.create(
						title = title, 
						link = request.data['link'], 
						category = request.data['category']
					)
					for t in tags:
						obj, created = tag.objects.get_or_create(name=t)
					
					tagObjList = tag.objects.filter(name__in = tags)
					tutorialObject.tags.set(tagObjList)
					return JSONResponse({"message " : "Created, Thanks" }, status=status.HTTP_201_CREATED)
			return JSONResponse({"message " : "Created, Thanks" }, status=status.HTTP_201_CREATED)
		return JSONResponse({"message":"Not Valid, Try Again"}, status=status.HTTP_406_NOT_ACCEPTABLE)