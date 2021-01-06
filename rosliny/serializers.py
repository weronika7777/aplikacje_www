from rest_framework import serializers
from .models import Rosliny
from .models import Rynek
from django.contrib.auth.models import User
class RoslinySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rosliny
        fields = '__all__'

class RynekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rynek
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'last_login', 'username', 'email', 'date_joined']