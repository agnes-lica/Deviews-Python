from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Post
from users.models import User
from users.permissions import IsAccountOwner, IsAccountOwnerOrdAdm

from .models import Comment
from .serializers import CommentSerializer


class CommentsView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = CommentSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        post_obj = get_object_or_404(Post, pk=self.kwargs["pk"])
        user_obj = get_object_or_404(User, id=self.request.user.id)
        serializer.save(post=post_obj, user=user_obj)


class CommentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrdAdm]

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
