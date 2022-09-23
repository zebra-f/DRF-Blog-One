from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from time import sleep

from blog.models import Post
from .serializers import PostSerializer
from .permissions import PostUserUpdateDeletePermission


class ReactTest(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        react_test = {
            'test': 'passed, you\'re authenticated'
        }
        return Response(react_test) 


# class PostList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         # slowing down this endpoint for a front-end testing 
#         sleep(1.0)
#         return super().get_queryset()
    

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [PostUserUpdateDeletePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [PostUserUpdateDeletePermission]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


    def list(self, request, *args, **kwargs):
        sleep(1.0)
        return super().list(request, *args, **kwargs)


