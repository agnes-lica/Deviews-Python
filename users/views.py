from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User
from .permissions import IsAccountOwnerOrdAdm, IsAdm, IsLogged
from .serializers import UserIsActiveSerializer, UserListSerializer, UserSerializer


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UsersListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdm]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersSearchView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLogged]

    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserSearchView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrdAdm]

    queryset = User
    serializer_class = UserListSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrdAdm]

    queryset = User
    serializer_class = UserSerializer


class UserIsActiveView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrdAdm]

    queryset = User
    serializer_class = UserIsActiveSerializer
