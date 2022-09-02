from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Post
from .serializers import PostSerializer
from .permissions import PostUserUpdateDeletePermission


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        # slowing down this endpoint for a front-end testing 
        # from time import sleep
        # sleep(2.0)
        return super().get_queryset()
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [PostUserUpdateDeletePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer







