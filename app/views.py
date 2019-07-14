from django.views.generic import TemplateView, ListView, FormView
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from . models import tag, tutorial
import re
from django.core.paginator import Paginator
from parser import parser

class HomePageView(TemplateView):
    template_name = 'home.html'


def search_query(request):
    query = request.GET.get('q')
    tutorialType = request.GET.get('ttype')
    list_query = query.split()
    object_list = tutorial.objects.filter(
        (Q(title__icontains=query) | Q(tags__name__in=list_query)) & Q(category__icontains=tutorialType)
    ).distinct()
    context = {'tquery':query, 'object_list':object_list}
    paginator = Paginator(context, 10)
    return render(request, 'search_results.html', context)


class ContributeView(TemplateView):
    def get(self, request):
        return render(request, 'contribute.html')
    
    def post(self, request):
        """
        Validate data here from request.POST and 
        run the parser & update database.
        """
        return render(request, 'thankyou.html')