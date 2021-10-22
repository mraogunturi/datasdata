from django.shortcuts import render
import json
# Create your views here.
from rest_framework import generics, permissions, response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import UserSerializer, DevelopersSerializer, InputSerializer
from django.http import JsonResponse, HttpResponse


class Developers(generics.ListAPIView):
    queryset = Developers.objects.all()
    serializer_class = DevelopersSerializer

    # def get_object(self):
    #     pk=self.kwargs.get('pk')
    #     return Developers.objects.get(pk=pk)


class Users(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer


@api_view(['GET'])
def Apijson(request):
    apidata = {
        'first_name':'mahesh',
        'last_name':'gunturi'
    }
    jsondum= json.dumps(apidata)
    return HttpResponse(jsondum)


@api_view(["GET"])
def UsersOutput(request):
    queryset = Apis.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = InputSerializer(queryset, many=True)
    return Response(serializer_class.data)


@api_view(["GET"])
def UserOutput(request, pk):
    queryset = Apis.objects.get(id=pk)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = InputSerializer(queryset, many=False)
    return Response(serializer_class.data)


@api_view(["POST"])
def UserInput(request):
    # queryset = Users.objects.get(id=pk)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = InputSerializer(data=request.data)

    if serializer_class.is_valid():
        serializer_class.save()

    return Response(serializer_class.data)


@api_view(["POST"])
def UserUpdate(request, pk):
    queryset=Apis.objects.get(id=pk)
    serializer_class = InputSerializer(instance=queryset,data=request.data)

    if serializer_class.is_valid():
        serializer_class.save()

    return Response(serializer_class.data)


@api_view(["DELETE"])
def UserDelete(request, pk):
    queryset=Apis.objects.get(id=pk)
    queryset.delete()

    return Response('Item deleted')


