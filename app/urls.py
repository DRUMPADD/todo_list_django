from django.urls import path
from django.contrib.auth import views as authV
from . import views
from .forms import PrettyAuthenticationForm

urlpatterns = [
    path('', views.index, name='principal'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', authV.LogoutView.as_view(), name='logout'),
    path('updateTask', views.updateTask, name='update'),
    path('deleteTask', views.deleteTask, name='delete'),
]