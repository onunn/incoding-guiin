from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.list, name='list'),
    
    path('test/', views.test, name='test'),
    path('<int:youtuber_id>/create/', views.create, name='create'),
    # path('restaurant/<int:restaurant_id>/review/create', views.review_create, name='review-create'),
    path('<int:youtuber_id>youtuber_list/', views.youtuber_list, name='youtuber_list'),

    path('list_test/', views.list_test, name='list_test'),
]