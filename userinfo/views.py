from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from userinfo.models import User
from userinfo.serializers import UserSerializer

# Create your views here.

class ListUser(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpdateUser(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeleteUser(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


