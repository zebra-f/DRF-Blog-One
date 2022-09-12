from django.urls import path

from .views import PostList, PostDetail, ReactTest


app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailupdatedelete'),
    path('', PostList.as_view(), name='listcreate'),
    path('reacttest', ReactTest.as_view(), name='reacttest'),
]