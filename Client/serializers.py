# client_api/serializers.py

from rest_framework import serializers
from .models import ClientUser

class ClientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUser
        fields =  '__all__'
