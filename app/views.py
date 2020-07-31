import time
import logging

logger = logging.getLogger(__name__)

from django.core.cache import cache
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
from taggie.parser import generate_tags
from .models import Tag, Tutorial
from . import cache_constants


class HomePageView(TemplateView):
    template_name = 'home.html'
    context = {}

    def get_context_data(self, **kwargs):
        """providing additional context"""
        self.context = super().get_context_data(**kwargs)
        self.context['categories'] = Tutorial.CATEGORIES
        return self.context


def search_query(request):
    """view for the search results
    search results (that meet category constraint) are prioritized by:
    1 - Title contains the exact keyword(s)
    2 - Tags contain the exact keyword(s)
    3 - Title contains partial keyword matches
    """
    try:
        # if somehow query is an empty string
        query = request.GET.get('q').lower().strip()
    except AttributeError:
        # pretend it's a space
        query = " "
    category = request.GET.get('category')
    list_query = query.split()

    start_time = time.time()

    # Begin with Category-valid Tutorials
    all_tutorials = Tutorial.objects.filter(category=category) if category else Tutorial.objects.all()
    logger.debug(f"all tutorials {all_tutorials}")
    if len(list_query):
        # Get all Tutorials with partial keyword matches in title OR exact keyword titles in tags
        partial_title_matches = Q()
        for keyword in list_query:
            logger.debug(f"Keyword is {keyword}")
            partial_title_matches.add(Q(title__icontains=keyword), Q.OR)

        filtered_tutorials = all_tutorials.filter(
            Q(tags__name__in=list_query) | partial_title_matches
            ).filter(publish=True).distinct()
        
        # Now to do this sorting operation, we'll have to convert to a list     
        def relevance_order(tut):
            title_set = set(tut.title.lower().split())
            logger.debug(f"titleset is {title_set}")
            query_set = set(list_query)
            logger.debug(f"queryset is {query_set}")
            tag_set = set(tut.tags.values_list('name', flat=True))
            logger.debug(f"tagset is {tag_set}")
            title_score = len(title_set & query_set)
            tag_score = len(tag_set & query_set)
            # give more weight to exact title matches
            logger.debug(f"{tut}: {title_score}*5 + {tag_score}")
            return -(title_score *5 + tag_score)

        sorted_tutorials = sorted(filtered_tutorials, key=relevance_order)
        logger.debug(f"filtered_tut is {filtered_tutorials}")
        logger.debug(f"sorted_tut is {sorted_tutorials}")
        
    else:
        # no need to go through all this trouble if user searched an empty string!
        sorted_tutorials = all_tutorials



    # if category is not None:
    #     tutorials = Tutorial.objects.filter(
    #         (Q(title__icontains=query) | Q(tags__name__in=list_query))
    #         & Q(category__icontains=category)
    #     ).order_by('id').filter(publish=True).distinct()
    # else:
    #     tutorials = Tutorial.objects.filter(
    #         (Q(title__icontains=query) | Q(tags__name__in=list_query))
    #     ).order_by('id').filter(publish=True).distinct()
    end_time = time.time()
    total = len(sorted_tutorials)
    result_time = round(end_time - start_time, 3)

    paginator = Paginator(sorted_tutorials, 3)
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
    tags = cache.get_or_set(cache_constants.ALL_TAGS, Tag.objects.all(), None)
    context = {
        'tags': tags,
        'title': 'Tags'
    }
    return render(request, 'tags.html', context)


def taglinks(request, tagname):
    """view for the tutorials with the {tagname}"""
    taglist = []
    taglist.append(tagname)
    # tutorials = Tag.objects.get(name = tagname).tutorial_set.all().filter(publish=True)
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
        link_count = Tutorial.objects.filter(
            link=request.POST['tlink']).count()
        if link_count == 0:
            tags, title = generate_tags(request.POST['tlink'])
            self.context['error'] = 'Not a Tutorial Link, Try Again'
            if 'other' in tags:
                return render(
                    request,
                    'contribute.html',
                    self.context
                )
            else:
                tutorial_object = Tutorial.objects.create(
                    title=title,
                    link=request.POST['tlink'],
                    category=request.POST['tcategory']
                )
                for tag in tags:
                    obj, created = Tag.objects.get_or_create(name=tag)

                tag_obj_list = Tag.objects.filter(name__in=tags)
                tutorial_object.tags.set(tag_obj_list)

                # clearing the all tags cache
                cache.delete(cache_constants.ALL_TAGS)
        # thankyou.html shouldn't be accessible unless someone successfully posts
        # a tutorial
                return render(request, 'thankyou.html', {'title': 'Thanks!'})
        return render(request, 'thankyou.html', {'title': 'Thanks!'})
