from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Response, Request, status

from .models import User
from .permissions import IsAccountOwnerOrdAdm, IsAdm, IsLogged
from .serializers import UserIsActiveSerializer, UserListSerializer, UserSerializer

from .models import User

class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(techs=self.request.data["techs"])

#  def post(self, request: Request) -> Response:
#         # techs = [TechSerializer(get_object_or_404(Tech, id=tech)).data for tech in request.data["techs"]]
#         # # print(request.data)
#         # request.data["techs"] = techs
#         # print(request.data)
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status.HTTP_201_CREATED)



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
