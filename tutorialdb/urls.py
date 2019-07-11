from django.contrib import admin
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
