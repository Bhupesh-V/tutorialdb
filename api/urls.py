from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='api-home'),
    path('tutorials/', views.tutorials),
    path('tutorials/<str:tags>/', views.tutorial_tag),
    path('tutorials/<str:tags>/<str:category>/', views.tutorial_tag_category),
    path('tags/', views.tags),
    path('latest/', views.latest),
]
