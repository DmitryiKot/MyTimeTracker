from django.urls import path
from django.contrib.auth import views

from . import views as my_views

app_name = 'trackerApp'

urlpatterns = [
    path('login/', views.LoginView.as_view(),
         name='login'),
    path('logout/', views.LogoutView.as_view(),
         name='logout'),
    path('profile/', my_views.view_profile,
         name='profile'),
    path('register/', my_views.register,
         name='register'),
]