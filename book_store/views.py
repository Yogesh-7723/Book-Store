from django.shortcuts import render
from .serializers import Registration,BookSerializer
from .models import User,Book
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication

from .perms import CustomPermission


# Create your views here.

class RegistrationApi(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Registration

class BookApi(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [CustomPermission]


    