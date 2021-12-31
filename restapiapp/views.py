from django.shortcuts import render
import json
import logging
# Create your views here.
from rest_framework import generics, permissions, response, serializers, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from restapiapp import models
from .models import *
from .models import Users as UserModel
from .serializers import UserSerializer, DevelopersSerializer, InputSerializer, UserCarSerializer
from django.http import Http404, HttpResponse, JsonResponse

class Developers(generics.ListCreateAPIView):
    queryset = Developers.objects.all()
    serializer_class = DevelopersSerializer

    # def get_object(self):
    #     pk=self.kwargs.get('pk')
    #     return Developers.objects.get(pk=pk)


# class Users(generics.ListCreateAPIView):
#     queryset = Users.objects.all()
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     serializer_class = UserSerializer


class UsersList(APIView):
    serializer_class=UserSerializer
    def get(self, request):
        querysetsdata = UserModel.objects.all()
        serializer = UserSerializer(querysetsdata, many=True)
        return Response(serializer.data)

    def post(self,request):
        data={
            'id':request.data.get('id'),
            'first_name':request.data.get('first_name'),
            'last_name':request.data.get('last_name'),
            'city':request.data.get('city')
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class UsersDetail(APIView):
    """
    Retrieve, update or delete a transformer instance
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = UserSerializer(transformer)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = UserSerializer(transformer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = UserSerializer(transformer,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
  
    def delete(self, request, pk, format=None):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



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



@api_view(["GET"])
def UsersApis(request):
    queryset=UserCarSerializer.objects.all()
    serializers_class=InputSerializer(queryset.get(id))
    return Response(serializers_class.data)

