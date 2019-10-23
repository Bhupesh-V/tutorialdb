from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer

from app.models import Tag, Tutorial
from app.views import handle_tutorial_post_request
from .serializers import TagSerializer, TutorialPOST, TutorialSerializer


@api_view(['GET'])
def index(request):
    """index view for api"""
    return render(request, 'api.html', {'title': 'API'})


class JSONResponse(HttpResponse):
    """wraps a simple HTTP Response to a JSON Response"""

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', 'POST'])
def tutorials(request):
    """
    get: Return all tutorials
    post: submit a tutorial
    """
    if request.method == 'GET':
        paginator = PageNumberPagination()
        tutorials = Tutorial.objects.all().order_by('id').filter(publish=True)
        context = paginator.paginate_queryset(tutorials, request)
        serializer = TutorialSerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        postserializer = TutorialPOST(data=request.data)
        if postserializer.is_valid():
            link = request.data['link']
            category = request.data['category']
            result = handle_tutorial_post_request(link, category)
            if result is not None:
                if result:
                    return JSONResponse(
                        {"message ": "Not a Tutorial link"},
                        status=status.HTTP_406_NOT_ACCEPTABLE
                    )
                return JSONResponse(
                    {"message ": "Created, Thanks"}, status=status.HTTP_201_CREATED
                )
            return JSONResponse(
                {"message ": "Created, Thanks"}, status=status.HTTP_201_CREATED
            )
        return JSONResponse(
            {"message": "Not Valid, Try Again"}, status=status.HTTP_406_NOT_ACCEPTABLE
        )


@api_view(['GET'])
def tutorial_tag(request, tags):
    """returns tutorials with {tags}"""
    paginator = PageNumberPagination()
    tags = tags.split(',')
    custom_tutorial = Tutorial.objects.filter(
        tags__name__in=tags).order_by('id').distinct().filter(publish=True)
    context = paginator.paginate_queryset(custom_tutorial, request)
    serializer = TutorialSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def tutorial_tag_category(request, tags, category):
    """return tutorials with {tags} and a {category}"""
    paginator = PageNumberPagination()
    tags = tags.split(',')
    category = category.split(',')
    custom_tutorial = Tutorial.objects.filter(
        tags__name__in=tags, category__in=category
    ).order_by('id').filter(publish=True).distinct()
    context = paginator.paginate_queryset(custom_tutorial, request)
    serializer = TutorialSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def tags(request):
    """returns all tags"""
    paginator = PageNumberPagination()
    tags = Tag.objects.all().order_by('id')
    context = paginator.paginate_queryset(tags, request)
    serializer = TagSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def latest(request):
    """returns latest 10 tutorials from tutorialdb"""
    paginator = PageNumberPagination()
    results = Tutorial.objects.all().filter(publish=True).order_by('-created_date')[:10]
    context = paginator.paginate_queryset(results, request)
    serializer = TutorialSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)
