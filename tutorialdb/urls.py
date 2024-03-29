from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('app.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
