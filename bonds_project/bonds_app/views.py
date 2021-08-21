from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .serializers import BondSerializer
from .models import Bond

# Create your views here.


def hello_world(request):
    data = {
        'message': 'Hello world'
    }
    return JsonResponse(data)


# class BondListView(generics.ListAPIView):
#     serializer_class = BondSerializer
#     queryset = Bond.objects.all()


# class BondRetrieveView(generics.RetrieveAPIView):
#     serializer_class = BondSerializer
#     queryset = Bond.objects.all()


class BondListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = BondSerializer
    queryset = Bond.objects.all()


class BondRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    # permission_classes = (IsAuthenticated, )

    serializer_class = BondSerializer
    queryset = Bond.objects.all()
