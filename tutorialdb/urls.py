from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from graphene_django.views import GraphQLView 

urlpatterns = [
    path('', include('app.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)), 
]
