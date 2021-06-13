
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]