import time

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView

from taggie.parser import generate_tags
from .models import Tag, Tutorial


class HomePageView(TemplateView):
    template_name = 'home.html'
    context = {}

    def get_context_data(self, **kwargs):
        """providing additional context"""
        self.context = super().get_context_data(**kwargs)
        self.context['categories'] = Tutorial.CATEGORIES
        return self.context


def search_query(request):
    """view for the search results"""
    query = request.GET.get('q').lower()
    category = request.GET.get('category')
    list_query = query.split()

    start_time = time.time()

    if category is not None:
        tutorials = Tutorial.objects.filter(
            (Q(title__icontains=query) | Q(tags__name__in=list_query))
            & Q(category__icontains=category)
        ).order_by('id').filter(publish=True).distinct()
    else:
        tutorials = Tutorial.objects.filter(
            (Q(title__icontains=query) | Q(tags__name__in=list_query))
        ).order_by('id').filter(publish=True).distinct()
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
        'query': query,
        'category': category,
        'tutorials': tutorials,
        'total': total,
        'time': result_time,
        'title': query,
        'categories': Tutorial.CATEGORIES
    }

    return render(request, 'search_results.html', context)


def latest(request):
    """view for the latest tutorial entries"""
    tutorials = Tutorial.objects.all().filter(publish=True).order_by('-id')[:10]
    context = {
        'tutorials': tutorials,
        'title': 'Latest'
    }
    return render(request, 'latest.html', context)


def tags(request):
    """view for the tags"""
    tags = Tag.objects.all()
    context = {
        'tags': tags,
        'title': 'Tags'
    }
    return render(request, 'tags.html', context)


def taglinks(request, tagname):
    """view for the tutorials with the {tagname}"""
    taglist = []
    taglist.append(tagname)
    tutorials = Tutorial.objects.filter(tags__name__in=taglist, publish=True)
    context = {
        'tag': tagname,
        'tutorials': tutorials,
        'title': tagname
    }
    return render(request, 'taglinks.html', context)


def about(request):
    """about view"""
    return render(request, 'about.html', {'title': 'About'})


class ContributeView(TemplateView):
    """view for the tutorial contribution page"""
    context = {
        'title': 'Contribute',
        'categories': Tutorial.CATEGORIES
    }

    def get(self, request):
        """GET the contribution form"""
        try:
            if 'error' in self.context.keys():
                self.context.popitem()
        except KeyError:
            pass

        return render(request, 'contribute.html', self.context)

    def post(self, request):
        """POST a tutorial"""
        link = request.POST['tlink']
        category = request.POST['tcategory']
        result = handle_tutorial_post_request(link, category)
        if result is not None:
            self.context['error'] = 'Not a Tutorial Link, Try Again'
            if result:
                return render(
                    request,
                    'contribute.html',
                    self.context
                )
            else:
                # thankyou.html shouldn't be accessible unless someone successfully posts
                # a tutorial
                return render(request, 'thankyou.html', {'title': 'Thanks!'})
        return render(request, 'thankyou.html', {'title': 'Thanks!'})


def handle_tutorial_post_request(link, category):
    if Tutorial.objects.filter(
            link=link
    ).exists():
        tags, title = generate_tags(link)
        if 'other' in tags:
            return True
        else:
            tutorial_object = Tutorial.objects.create(
                title=title,
                link=link,
                category=category
            )
            tag_obj_list = []
            for tag in tags:
                obj, created = Tag.objects.get_or_create(name=tag)
                tag_obj_list.append(obj)

            tutorial_object.tags.set(tag_obj_list)
            return False
