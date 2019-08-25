from django.conf.urls import include
from django.urls import path
from . import views
from .views import ContributeView, HomePageView

app_name = 'app'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', views.search_query, name='search-results'),
    path('api/', include('api.urls'), name='api'),
    path('latest/', views.latest, name='latest'),
    path('tags/', views.tags, name='tags'),
    path('tags/tag=<tagname>', views.taglinks, name='tag-links'),
    path('about/', views.about, name='about'),
    path('contribute/', ContributeView.as_view(), name='contribute'),
]
