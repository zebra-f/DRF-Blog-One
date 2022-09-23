from django.urls import path, include

from rest_framework.routers import DefaultRouter

# from .views import PostList, PostDetail, ReactTest
from .views import ReactTest, PostViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet,basename="posts")

app_name = 'blog_api'

urlpatterns = [
    # path('<int:pk>/', PostDetail.as_view(), name='detailupdatedelete'),
    # path('', PostList.as_view(), name='listcreate'),
    path('', include(router.urls)),
    path('reacttest', ReactTest.as_view(), name='reacttest'),
]