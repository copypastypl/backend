from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='create-user'),
    path('login/', views.UserLoginView.as_view(), name='login-user'),
    path('profile/', views.UserDetailView.as_view(), name='detail-user')
]
