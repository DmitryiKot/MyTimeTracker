from django.urls import path
from django.contrib.auth import views

app_name = 'trackerApp'

urlpatterns = [
    path('login/', views.LoginView.as_view(),
         name='login'),
    path('logout/', views.LogoutView.as_view(),
         name='logout'),
]