from django.urls import path

from .views import ListToDo, DetailTodo

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListToDo.as_view()),
]
