from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from .serializers import PostSerializer

from blog.models import Post


class PostDetail(RetrieveDestroyAPIView):
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer


class PostList(ListCreateAPIView):
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer
