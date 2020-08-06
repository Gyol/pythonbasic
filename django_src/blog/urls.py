from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/ 이런식으로 올거잖아 그니까 뒤에 암거도 안온다는거
    path('', views.post_list, name='post_list'), # 그래서 앞에 ''한겨
    # localhost:8000/post/5 (=id)
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # localhost:8000/post/new
    path('post/new', views.post_new, name='post_new'),
    # localhost:8000/post/5/edit
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/remove', views.post_remove, name='post_remove'),
]