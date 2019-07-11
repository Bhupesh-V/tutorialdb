from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('', views.index),
    path('tutorials/<str:tags>/', views.tutorial_Tags),
    path('tutorials/<str:tags>/<str:ttype>/', views.tutorial_Tags_Type),
    path('tutorials/', views.tutorials),
    path('tags/', views.tags),
]