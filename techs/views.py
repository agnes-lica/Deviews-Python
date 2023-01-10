from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdm
from django.shortcuts import get_object_or_404
from .models import Tech
from .serializers import TechSerializer
from rest_framework.views import Response, Request, status

class TechView(generics.CreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAdm]

    queryset = Tech.objects.all()
    serializer_class = TechSerializer

class TechListView(generics.ListAPIView):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer

class TechDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdm]

    queryset = Tech.objects.all()
    serializer_class = TechSerializer
