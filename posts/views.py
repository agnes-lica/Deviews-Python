from rest_framework import generics
from .serializers import PostSerializer
from .models import Post


class PostView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    ...
