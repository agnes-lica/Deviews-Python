from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer
from .models import Post
from users.models import User
from techs.models import Tech
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAccountOwnerOrdAdm


class PostView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        user_obj = get_object_or_404(User, id = self.request.user.id)
        tech_obj = get_object_or_404(Tech, id = self.request.data["tech"])
        serializer.save(user=user_obj, tech=tech_obj)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrdAdm]

    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostUserDetailViews(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().filter(user_id=self.kwargs["pk"])