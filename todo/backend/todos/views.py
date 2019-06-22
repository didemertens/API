from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

class ListToDo(generics.ListAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer

class DetailTodo(generics.ListAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer
