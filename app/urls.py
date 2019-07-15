from django.urls import path
from .views import HomePageView,ContributeView
from django.conf.urls import include
from . import views


urlpatterns = [
    path('search/', views.search_query, name='search_results'),
    path('latest/', views.latest),
    path('', HomePageView.as_view(), name='home'),
    path('api/', include('api.urls')),
    path('contribute/', ContributeView.as_view()),
    path('thankyou/', ContributeView.as_view()),
]