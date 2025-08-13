from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from rest_framework.response import Response

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from .serializers import *

class UserCreateView(APIView):
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_201_CREATED)

class UserLoginUsername(APIView):
    def post(self, request):
        serializer = LoginUserUsernameSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(username=username)
                if user.password == password:
                    return Response({
                        'message': 'Login successful',
                        'user': {
                            'id': user.id,
                            'username': user.username,
                            'email': user.email
                        }
                    })
                else:
                    return Response({'error': 'Invalid password'}, status=HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UserLoginEmail(APIView):
    def post(self, request):
        serializer = LoginUserEmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(email=email)
                if user.password == password:
                    return Response({
                        'message': 'Login successful',
                        'user': {
                            'id': user.id,
                            'username': user.username,
                            'email': user.email
                        }
                    })
                else:
                    return Response({'error': 'Invalid password'}, status=HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)