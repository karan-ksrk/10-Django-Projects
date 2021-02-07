from django.urls import path
from . views import  *

urlpatterns = [
    path('add_post/', add_post.as_view()),
    path('update_post/<str:id>', update_post.as_view()),
    path('delete_post/<int:id>', delete_post.as_view()),
    path('read_post/<int:id>', read_post.as_view()),
    path('read_post_all/', read_post_all.as_view()),
]
