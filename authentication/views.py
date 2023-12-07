from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.viewsets import ViewSet

from authentication.models import User
from authentication.serializers import LoginSerializer, RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
class LoginView(TokenViewBase):
    serializer_class = LoginSerializer
