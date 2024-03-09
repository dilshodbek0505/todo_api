from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer


class UserRegisterApi(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status": True,
            "data": serializer.data
        })

class UserLoginApi(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        login(request=request, user = user)
        return Response({
            "status": True,
            "data": "Foydalanuvchi tizimga kiritildi !"
        })

class UserApi(APIView):
    def get_object(self, pk):
        return User.objects.get(id = pk)

    def get(self, request, pk, *args, **kwargs):
        user = self.get_object(pk)
        serializer = UserSerializer(instance=user)
        return Response({
            "status": True,
            "data": serializer.data
        })

    def patch(self, request, pk, *args, **kwargs):
        user = self.get_object(pk)
        serializer = UserSerializer(instance=user, data=request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status": True,
            "data": serializer.data
        })

    def delete(self, request, pk, *args, **kwargs):
        user = self.get_object(pk)
        user.delete()
        return Response({
            "status": True,
            "data": "Foydalanuvchi ma'lumotlari o'chirildi!"
        })
