from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import User, Zahtjev
from .serializers import UserSerializer, ZahtjevSerializer

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ZahtjevView(viewsets.ModelViewSet):
    queryset = Zahtjev.objects.all()
    serializer_class = ZahtjevSerializer
    permission_classes = [permissions.AllowAny]

