from django.conf.urls import include
from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import ContributeView, HomePageView

app_name = 'app'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', views.search_query, name='search-results'),
    path('tutorial/<int:pk>', views.tutorial_redirect, name='tutorial_redirect'),
    path('api/', include('api.urls'), name='api'),
    path('latest/', views.latest, name='latest'),
    path('tags/', views.tags, name='tags'),
    path('tags/tag=<tagname>', views.taglinks, name='tag-links'),
    path('about/', views.about, name='about'),
    path('contribute/', ContributeView.as_view(), name='contribute'),
    path('service-worker.js', TemplateView.as_view(
    template_name="service-worker.js",
    content_type='application/javascript',
), name='service-worker.js'),
]