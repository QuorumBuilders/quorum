from rest_framework import serializers
from library.models import Resource, ResourceCategory, Course

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class ResourceCategory(serializers.ModelSerializer):
    class Meta:
        model = ResourceCategory
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields  = '__all__'
