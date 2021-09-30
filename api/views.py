from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# Create your views here.


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        # token = Token.objects.get(key=response.data['token'])
        return Response({'user': UserSerializer(request.user).data})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['GET'])
    def profile(self, request):
        try:
            return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)
        except:
            response = {'message': 'No token provided'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


