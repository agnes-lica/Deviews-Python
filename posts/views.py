from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer
from .models import Post
from users.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAccountOwnerOrdAdm


class PostView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # def perform_create(self, serializer):
    #     user_obj = get_object_or_404(User, pk=self.kwargs["pk"])
    #     serializer.save(user=user_obj)


class PostUpdateView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrdAdm]

    serializer_class = PostSerializer
    queryset = Post


class PostDestroyView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrdAdm]

    serializer_class = PostSerializer
    queryset = Post


class PostDetailView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostUserDetailViews(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().filter(user_id=self.kwargs["pk"]).values()

        
    # queryset = Post.objects.filter(user=self.request.user)
    # queryset = Post.objects.all().filter(user_id = self.kwargs["pk"])

    # def retrieve(self, request, *args, **kwargs):

    #     instance = get_object_or_404(User, pk=self.kwargs["pk"])
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
