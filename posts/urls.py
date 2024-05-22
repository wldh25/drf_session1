# posts > urls.py
from django.urls import path, include
from .views import *

app_name = 'posts'

urlpatterns = [
    path('post/', PostAPIView.as_view()),
    path('list/', GetlistAPIView.as_view()),
    path('comment/',CommentAPIView.as_view()),
    # path('post/', PostAPIView2.as_view()),
]