from django.urls import path

from .views import UserRegisterApi, UserLoginApi, UserApi

urlpatterns = [
    path('register/', UserRegisterApi.as_view()),
    path('login/', UserLoginApi.as_view()),
    path('details/<int:pk>/', UserApi.as_view())
]
