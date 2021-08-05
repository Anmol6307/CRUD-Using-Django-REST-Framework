from django.db.models import fields
from rest_framework import serializers
from userinfo.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'state', 'city']
