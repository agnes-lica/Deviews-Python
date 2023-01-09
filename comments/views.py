from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

from users.permissions import IsAccountOwner, IsAccountOwnerOrdAdm
from .models import Comment
from .serializers import CommentSerializer
from posts.models import Post



class commentsView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = CommentSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        post_obj = get_object_or_404(Post, pk=self.kwags["pk"])
        serializer.save(post=post_obj)


class commentsViewDelete(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrdAdm]

    serializer_class = CommentSerializer

    def delete(self, request, comment_id: int):
        comment = get_object_or_404(Comment, pk=self.kwargs["pk"])
        comment.delete()
