from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from django.contrib.auth.models import User
from .serializers import (UserSerializer, BondSerializer)
from .models import Bond

# Create your views here.


def hello_world(request):
    data = {
        'message': 'Hello world'
    }
    return JsonResponse(data)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BondListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = BondSerializer
    queryset = Bond.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BondRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = BondSerializer
    queryset = Bond.objects.all()
