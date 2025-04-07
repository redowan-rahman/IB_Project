from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authentication_views
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('', include('users.urls')), # inter mapping
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
