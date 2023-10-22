from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
  path('', views.index, name='index'),
  path('signUp/', views.signUp, name='signUp'),
  path('login/',views.login,name='login'),
  path('question/', views.CreateQuestion, name='question'),
  #path('process', views.process, name='process'),
]
