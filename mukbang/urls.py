from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.list, name='list'),
    
  
    path('create/', views.create, name='create'),
    path('test/', views.test, name='test'),
    path('list_test/', views.list_test, name='list_test'),
]