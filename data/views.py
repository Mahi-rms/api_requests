from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import Data
from .serializers import DataSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def AddData(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def ShowData(request):
    products = Data.objects.all()
    serializer = DataSerializer(products, many=True)
    return Response(serializer.data)

def index(request):
    return render(request,'index.html')