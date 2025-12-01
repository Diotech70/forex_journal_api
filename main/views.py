from django.shortcuts import render
from .models import Journal
from .serializers import RegisterSerializer, JournalSerializer
from rest_framework import generics, permissions, viewsets
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
      serializer_class = RegisterSerializer
      permission_classes = [permissions.AllowAny]
      queryset = User.objects.all()
class ProfileView(APIView):
      permission_classse=[permissions.IsAuthenticated]
      def get(self,request):
          user=request.user
          return Response({'username':user.username,'email':user.email,'message':f'Welcome Back {user.username}'})

class JournalView(viewsets.ModelViewSet): 
      serializer_class = JournalSerializer  
      queryset = Journal.objects.all()
      
# Create your views here.
