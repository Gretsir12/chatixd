from rest_framework import serializers
from .models import *

class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=50,
        min_length=3,
        error_messages={
            'min_length': 'Имя пользователя должно содержать минимум 3 символа',
            'max_length': 'Имя пользователя не может быть длиннее 50 символов'
        }
    )
    password = serializers.CharField(
        max_length=50,
        min_length=6,
        error_messages={
            'min_length': 'Пароль должен содержать минимум 6 символов',
            'max_length': 'Пароль не может быть длиннее 50 символов'
        }
    )
    email = serializers.CharField(
        max_length=50,
        error_messages={
            'max_length': 'Email не может быть длиннее 50 символов'
        }
    )
    
    class Meta:
        model = User
        fields = '__all__'

class LoginUserUsernameSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=50,
        min_length=3,
        error_messages={
            'required': 'Имя пользователя обязательно',
            'min_length': 'Имя пользователя должно содержать минимум 3 символа',
            'max_length': 'Имя пользователя не может быть длиннее 50 символов'
        }
    )
    password = serializers.CharField(
        max_length=50,
        min_length=6,
        error_messages={
            'required': 'Пароль обязателен',
            'min_length': 'Пароль должен содержать минимум 6 символов',
            'max_length': 'Пароль не может быть длиннее 50 символов'
        }
    )

class LoginUserEmailSerializer(serializers.Serializer):
    email = serializers.CharField(
        max_length=50,
        error_messages={
            'required': 'Email обязателен',
            'max_length': 'Email не может быть длиннее 50 символов'
        }
    )
    password = serializers.CharField(
        max_length=50,
        min_length=6,
        error_messages={
            'required': 'Пароль обязателен',
            'min_length': 'Пароль должен содержать минимум 6 символов',
            'max_length': 'Пароль не может быть длиннее 50 символов'
        }
    )