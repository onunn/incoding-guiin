from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('update/', views.update, name="muckbang-update"),
    path('test/', views.test, name='test'),
    path('create/<int:group_id>', views.create, name='create'),
    # path('restaurant/<int:restaurant_id>/review/create', views.review_create, name='review-create'),
 
    path('question_test/',views.question_test, name="question_test"),
    path('youtuber/<int:group_id>',views.youtuber, name="youtuber"),
    path('group_list/', views.group_list, name='group_list'),

]
