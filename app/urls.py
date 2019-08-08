from django.urls import path
from .views import HomePageView,ContributeView
from django.conf.urls import include
from . import views

app_name = 'app'
urlpatterns = [
    path('search/', views.search_query, name='search-results'),
    path('latest/', views.latest, name='latest'),
    path('', HomePageView.as_view(), name='home'),
    path('api/', include('api.urls'), name='api'),
    path('contribute/', ContributeView.as_view(), name='contribute'),
    path('tags/', views.tags, name='tags'),
    path('thankyou/', ContributeView.as_view(), name='thankyou'),
    path('about', views.about, name='about'),
    path('tags/tag=<tagname>', views.taglinks, name='tag-links'),
]