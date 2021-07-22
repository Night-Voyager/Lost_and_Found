import django_filters.rest_framework

from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions

from .models import FindObject, FindOwner
from .serializers import FindObjectSerializer, FindOwnerSerializer
from .permissions import IsPublisherOrReadOnly
from apps.miniprogramAPI.views import Security

# Create your views here.
# 使用APIView


class FindObjectList(generics.ListCreateAPIView):
    # queryset = FindObject.objects.all()
    serializer_class = FindObjectSerializer

    def post(self, request):
        serializer = FindObjectSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer.validated_data)
            msg = []
            img = ''

            for k, v in serializer.validated_data.items():
                print(k, v)
                if k == 'objectImage':
                    img = v
                else:
                    msg.append(v)

            if Security().multiMsgSecCheck(msglist=msg)\
                    and (img == '' or (img != '' and Security().imgSecCheck(img=img))):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = FindObject.objects.all()
        publisher = self.request.query_params.get('publisher', None)
        if publisher is not None:
            queryset = queryset.filter(publisher=publisher)
        return queryset

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # def perform_create(self, serializer):
    #     serializer.save(publisher=self.request.publisher)


class FindObjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FindObject.objects.all()
    serializer_class = FindObjectSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsPublisherOrReadOnly)


class FindOwnerList(generics.ListCreateAPIView):
    # queryset = FindOwner.objects.all()
    serializer_class = FindOwnerSerializer

    def post(self, request):
        serializer = FindOwnerSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer.validated_data)
            msg = []
            img = ''

            for k, v in serializer.validated_data.items():
                print(k, v)
                if k == 'objectImage':
                    img = v
                else:
                    msg.append(v)

            if Security().multiMsgSecCheck(msglist=msg)\
                    and (img == '' or (img != '' and Security().imgSecCheck(img=img))):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = FindOwner.objects.all()
        publisher = self.request.query_params.get('publisher', None)
        if publisher is not None:
            queryset = queryset.filter(publisher=publisher)
        return queryset
    
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # def perform_create(self, serializer):
    #     serializer.save(publisher=self.request.publisher)


class FindOwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FindOwner.objects.all()
    serializer_class = FindObjectSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsPublisherOrReadOnly)


'''
class FindObjectView(APIView):
    def get(self, request, format=None):
        find_object = FindObject.objects.all()
        serializer = FindObjectSerializer(find_object, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FindObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FindOwnerView(APIView):
    def get(self, request, format=None):
        find_owner = FindOwner.objects.all()
        serializer = FindOwnerSerializer(find_owner, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FindOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
