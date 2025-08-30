# restaurant/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuItemSerializer(serializers.ModelSerializer):  # ✅ Rename here
    class Meta:
        model = Menu
        fields = '__all__'
