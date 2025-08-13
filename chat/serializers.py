from rest_framework import serializers
from .models import *
from registration.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class UserChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContact
        fields = '__all__'

class CreateContactSerializer(serializers.ModelSerializer):
    contact_username = models.CharField(
        max_length=50,
        error_messages={
            "max_length": "Длина не больше 50 символов"
        }
    )

    owner_username = models.CharField(
        max_length=50,
        error_messages={
            "max_length": "Длина не больше 50 символов"
        }
    )

    chat_id=models.CharField(
    )