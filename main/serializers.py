from .models import Journal
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
      password = serializers.CharField(write_only=True, validators=[validate_password])
      class Meta:
            model = User
            fields = ['username','email','password']

      def create(self, validated_data):
          user = User.objects.create_user(username=validated_data['username'],email=validated_data.get('email',''),password=validated_data['password'],)
          return user

class JournalSerializer(serializers.ModelSerializer):
      class Meta:
            model = Journal
            fields =['id','user','pair','date','lot_size','entry','close','profit','loss','entry_time','close_time','notes']
            read_only_fields=['user']
