from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authentication_views
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('', include('users.urls')), # inter mapping
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
