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
    path('edit/', my_views.edit,
         name='edit'),
    path('', my_views.TaskListView.as_view(),
         name='all_tasks'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         my_views.high_level_task_details,
         name='high_level_task_details'),
    path('create/', my_views.create_form,
         name='create_form'),
    path('tasks/', my_views.LowTaskListView.as_view(),
         name='all_tasks_low'),
    path('<int:month>/<int:day>/<int:year>/<slug:slug>/',
         my_views.low_level_task_details,
         name='low_level_task_details'),
    path('create_low/', my_views.create_form_low,
         name='create_form_low'),
    path('<int:pk>/edit_high_task/', my_views.edit_task_high,
         name='edit_high_task'),
]