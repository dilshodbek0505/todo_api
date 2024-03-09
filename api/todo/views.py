from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Todo
from .serializers import TodoSerializer


@method_decorator(csrf_exempt, name='post')
class TodoApi(APIView):
    def get_object(self, pk):
        return Todo.objects.get(id = pk)
     
    def post(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status": True,
            "data": serializer.data
        })

    def get(self, request, pk, *args, **kwargs):
        todo = self.get_object(pk)
        serializer = TodoSerializer(instance=todo)
        return Response({
            "status": True,
            "data": serializer.data
        })
    
    def patch(self, request, pk, *args, **kwargs):
        todo = self.get_object(pk)
        serializer = TodoSerializer(instance=todo, data=request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status": True,
            "data": serializer.data
        })
    
    def delete(self, request, pk, *args, **kwargs):
        todo = self.get_object(pk)
        todo.delete()
        return Response({
            "status": True,
            "data": "Ma'lumotlar o'chirildi!"
        })
    
class ShowAllTodoApi(APIView):
    def get(self,request, *args, **kwargs):
        todos = Todo.objects.all()
        serializer = TodoSerializer(instance=todos, many = True)
        return Response({
            "status": True,
            "data": serializer.data
        })
