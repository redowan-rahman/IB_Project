from django.urls import path
from django.contrib.auth import views as authentication_views
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('profile/', views.profile, name = 'profile'),
    path('login/', authentication_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout/', views.logoutUser, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('get-appointment/', views.get_appointment, name='get_appointment'),
]
