from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('update/', views.update, name="muckbang-update"),
    path('test/', views.test, name='test'),
    path('create/<int:group_id>', views.create, name='create'),
    # path('restaurant/<int:restaurant_id>/review/create', views.review_create, name='review-create'),
 
    path('question/1',views.question1, name="question1"),
    path('question/2',views.question2, name="question2"),
    path('question/3',views.question2, name="question2"),

    path('youtuber/<int:group_id>',views.youtuber, name="youtuber"),
    path('group_list/', views.group_list, name='group_list'),
    path('result/<int:group_id>', views.result, name='result'),

]
