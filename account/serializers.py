from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['id', 'gender', 'bio', 'address_1', 'address_2', 'city', 'state', 'zip_code', 'phone_number', 'is_parent', 'is_teacher']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"