from django.views.generic import TemplateView, ListView, FormView
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from . models import tag, tutorial
import re
from . forms import TutorialForm

class HomePageView(TemplateView):
    template_name = 'home.html'

# class SearchResultsView(ListView):
#     model = tutorial
#     template_name = 'search_results.html'

def search_query(request):
    query = request.GET.get('q')
    tutorialType = request.GET.get('ttype')
    list_query = query.split()
    object_list = tutorial.objects.filter(
        (Q(title__icontains=query) | Q(tags__name__in=list_query)) & Q(category__icontains=tutorialType)
    ).distinct()
    context = {'tquery':query, 'object_list':object_list}
    print(context)
    return render(request, 'search_results.html', context)

class ContributeView(TemplateView):
    def get(self, request):
        #form = TutorialForm()
        return render(request, 'contribute.html')
    
    def post(self, request):
        #form = TutorialForm(self.request.POST)
        #if form.is_valid():
        # link = form.cleaned_data['link']
        # category = form.cleaned_data['category']
        # data = {'link': link, 'category': category}
        print(request.POST)
        return render(request, 'thankyou.html')