from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 255, write_only = True)
    confirm_password = serializers.CharField(max_length = 255, write_only = True)

    class Meta:
        model = User
        fields = ['id', 'username', 'confirm_password', 'password']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError("Paro to'g'ri kelmadi!")
        attrs['password'] = make_password(attrs['password'])
        attrs.pop('confirm_password')
        return attrs

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 255)
    password = serializers.CharField(max_length = 255, write_only = True)

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = authenticate(username = attrs.get('username'), password = attrs.get('password'))
        if not self.user:
            raise serializers.ValidationError("Foydalanuvch topilmadi !")        

        return attrs

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 255, write_only = True, required = True)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email','username','password']
    
    def validate(self, attrs):
        if attrs.get('password'):
            attrs['password'] = make_password(attrs['password'])
        return attrs

    