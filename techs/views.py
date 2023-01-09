from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAccountOwnerOrdAdm
from django.shortcuts import get_object_or_404
from .models import Tech
from .serializers import TechSerializer
from rest_framework.views import Response, Request, status


class techViewCreate(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrdAdm]

    def post(self, request: Request) -> Response:
        serializer_class = TechSerializer(data=request.data)
        techs = Tech.objects.all()

        tech_obj = get_object_or_404(Tech, pk=self.kwags["pk"])
        serializer_class.save(tech=tech_obj)

        return Response(serializer_class.data, status.HTTP_201_CREATED)

class techViewList(generics.CreateAPIView):
    def get(self, request: Request) -> Response:
        techs = Tech.objects.all()
        serializer_class = TechSerializer(techs, many=True)

        return Response(serializer_class.data)


class techViewPatchDelete(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrdAdm]

    def patch(self, request: Request, tech_id: int) -> Response:
        tech = get_object_or_404(Tech, pk=self.kwargs["pk"])
        serializer_class = TechSerializer(tech, data=request.data)
        serializer_class.is_valid(raise_exception=True)


        serializer_class.save()
        return Response(serializer_class.data)

    def delete(self, request: Request, tech_id: int):
        tech = get_object_or_404(Tech, pk=self.kwargs["pk"])
        tech.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
