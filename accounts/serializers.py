from rest_framework import serializers
from accounts.models import StudentProfile,FreshmanProfile, CustomUser as User
from rest_framework.exceptions import ValidationError
import re


class RegisterSerializer(serializers.ModelSerializer):
    # This Serializer is tailored for student registration.

    matric_no = serializers.CharField(max_length=12,write_only=True)
    class Meta:
        model = User
        fields = ['username','matric_no','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        matric_no = validated_data.pop('matric_no')
        if re.match(r"^CSC/\d{2}/\d{4}$", matric_no):
            ...
        else:
            raise ValidationError({
                'matric_no': 'This field does not satisfy the pattern CSC/00/0000.'
            })
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        StudentProfile.objects.create(user=user,matric_no=matric_no)
        return user

class FreshmanRegisterSerializer(serializers.ModelSerializer):
    # This Serializer is tailored for fresh/new student.
    # who are yet to get their matric number.
    # 

    registration_no = serializers.CharField(max_length=14,write_only=True)
    class Meta:
        model = User
        fields = ['username','registration_no','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        registration_no = validated_data.pop('registration_no')
        if re.match(r"^\d{4}\d{8}[A-Za-z]{2}$", registration_no):
            ...
        else:
            raise ValidationError({
                'registration_no': 'This field does not satisfy the pattern 202512345678AB.'
            })
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        FreshmanProfile.objects.create(user=user,registration_no=registration_no)
        return user