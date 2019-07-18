from django.views.generic import TemplateView, ListView, FormView
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from . models import tag, tutorial
import re
from django.core.paginator import Paginator
from taggie.parser import generateTags

class HomePageView(TemplateView):
    template_name = 'home.html'

def latest(request):
    results = tutorial.objects.all().order_by('-id')[:10]
    results = { 'results': results }
    return render(request, 'latest.html', results)

def search_query(request):
    query = request.GET.get('q')
    tutorialType = request.GET.get('ttype')
    list_query = query.split()
    object_list = tutorial.objects.filter(
        (Q(title__icontains=query) & Q(tags__name__in=list_query)) & Q(category__icontains=tutorialType)
    ).distinct()
    context = {'tquery':query, 'object_list':object_list}
    paginator = Paginator(context, 10)
    return render(request, 'search_results.html', context)


class ContributeView(TemplateView):
    def get(self, request):
        return render(request, 'contribute.html')
    
    def post(self, request):
        linkCount = tutorial.objects.filter(link = request.POST['tlink']).count()
        if linkCount == 0:
            tags, title = generateTags(request.POST['tlink'])
            tutorialObject = tutorial.objects.create(
                title = title, 
                link = request.POST['tlink'], 
                category = request.POST['tcategory']
            )
            tagObjList = tag.objects.filter(name__in = tags)
            tutorialObject.tags.set(tagObjList)
        return render(request, 'thankyou.html')