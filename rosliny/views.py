from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .models import Rosliny
from .models import Rynek
from .serializers import RoslinySerializer
from .serializers import RynekSerializer
from .serializers import UserSerializer
from rest_framework import permissions


class RoslinyList(generics.ListCreateAPIView):
    queryset = Rosliny.objects.all()
    serializer_class = RoslinySerializer
    name= 'rosliny'
    filter_fields=['gatunek']
    search_fields = ['wzrost','mrozoodporne']
    ordering_fields = ['gatunek']

class RynekList(generics.ListCreateAPIView):
    queryset = Rynek.objects.all()
    serializer_class = RynekSerializer
    name = 'rynek'
    filter_fields=['cena']
    permissions_classes = permissions.IsAuthenticated
    search_fields = ['ilosc','miejscowosc']
    ordering_fields = ['cena']

class RoslinyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rosliny.objects.all()
    serializer_class = RoslinySerializer
    name = 'roslina'
    permissions_classes = permissions.IsAuthenticated

class RynekDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rynek.objects.all()
    serializer_class = RynekSerializer
    name = 'ryneczek'
    permissions_classes = permissions.IsAuthenticated

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'users'
    permissions_classes = permissions.IsAuthenticated

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user'
    permissions_classes = permissions.IsAuthenticated

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'rosliny': reverse(RoslinyList.name, request=request),
                         'rynek': reverse(RynekList.name, request=request),
                         'users': reverse(UserList.name, request=request)
                         })