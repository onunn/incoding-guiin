from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.list, name='list'),

    path('test/', views.test, name='test'),
    path('passwd/', views.passwd, name='passwd')

]