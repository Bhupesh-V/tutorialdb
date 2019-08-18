from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import tag, tutorial
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggie.parser import generateTags
import time

class HomePageView(TemplateView):
	"""
	Home page view.
	"""
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = tutorial.CATEGORIES
		return context

def latest(request):
	"""
	View for the latest tutorial entries.
	"""
	tutorials = tutorial.objects.all().order_by('-id')[:10]
	context = {
		'tutorials': tutorials, 
		'title': 'Latest'
	}
	return render(request, 'latest.html', context)

def about(request):
	"""
	About view.
	"""
	return render(request, 'about.html', {'title': 'About'})

def search_query(request):
	"""
	View for the search results.
	"""
	query = request.GET.get('q').lower()
	category = request.GET.get('category')
	list_query = query.split()

	start_time = time.time()

	if category is not None:
		tutorials = tutorial.objects.filter(
			(Q(title__icontains=query) | Q(tags__name__in=list_query)) 
			& Q(category__icontains=category)
		).order_by('id').distinct()
	else:
		tutorials = tutorial.objects.filter(
			(Q(title__icontains=query) | Q(tags__name__in=list_query))
		).order_by('id').distinct()
	end_time = time.time()
	total = len(tutorials)
	result_time = round(end_time - start_time, 3)

	paginator = Paginator(tutorials, 3)
	page = request.GET.get('page')
	try:
		tutorials = paginator.page(page)
	except PageNotAnInteger:
		tutorials = paginator.page(1)
	except EmptyPage:
		tutorials = paginator.page(paginator.num_pages)

	context = {
		'query':query, 
		'tutorials':tutorials, 
		'total': total, 
		'time': result_time, 
		'title': query,
		'categories': tutorial.CATEGORIES
	}

	return render(request, 'search_results.html', context)

class ContributeView(TemplateView):
	"""
	View for the tutorial contribution page.
	"""
	def get(self, request):
		"""
		GET the contribution form.
		"""
		context = {
			'title': 'Contribute', 
			'categories': tutorial.CATEGORIES
		}
		return render(request, 'contribute.html', context)
	
	def post(self, request):
		"""
		POST a tutorial.
		"""
		linkCount = tutorial.objects.filter(link = request.POST['tlink']).count()
		if linkCount == 0:
			tags, title = generateTags(request.POST['tlink'])
			if 'other' in tags:
				return render(
					request, 
					'contribute.html', 
					{'error': "Not a Tutorial Link, Try Again"}
				)
			else:
				tutorialObject = tutorial.objects.create(
					title = title, 
					link = request.POST['tlink'], 
					category = request.POST['tcategory']
				)
				for t in tags:
					obj, created = tag.objects.get_or_create(name=t)

				tagObjList = tag.objects.filter(name__in = tags)
				tutorialObject.tags.set(tagObjList)
				return redirect('app:thankyou')
		return redirect('app:thankyou')

def tags(request):
	"""
	View for the tags.
	"""
	tags = tag.objects.all()
	context = {
		'tags':tags, 
		'title': 'Tags'
	}
	return render(request, 'tags.html', context)

def taglinks(request, tagname):
	"""
	View for the tutorials with the {tagname}.
	"""
	taglist = []
	taglist.append(tagname)
	tutorials = tutorial.objects.filter(tags__name__in = taglist)
	context = {
		'tag': tagname, 
		'tutorials':tutorials, 
		'title': tagname
	}
	return render(request, 'taglinks.html', context)

def thanks(request):
	return render(request, 'thankyou.html', {'title': 'Thanks'})