from django.urls import path
from .views import TodoApi, ShowAllTodoApi

urlpatterns = [
    path("details/<int:pk>/", TodoApi.as_view()),
    path("all/", ShowAllTodoApi.as_view()),
    path('create/', TodoApi.as_view())
]

