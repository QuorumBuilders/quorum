from rest_framework import serializers
from accounts.models import Profile, AbstractUser as User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','bio']