from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.list, name='list'),
    
    path('test/', views.test, name='test'),
    path('list_test/', views.list_test, name='list_test'),
    path('question_test/',views.question_test, name="question_test")
]