from rest_framework import serializers

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Group

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the user model
    """
    class Meta(object):
        model = User
        fields = ["id", "username", "password"]
        # Note: django requires username, but we only need email
        # username field actually contains email address
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8}
            }
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the Group model
    """
    class Meta(object):
        model = Group
        fields = ["name", "description",]
    def create(self, validated_data):
        members = self.context.get("request").user
        group_obj = Group.objects.create(**validated_data)
        group_obj.members.set([members])
        return group_obj

class AuthSerializer(serializers.Serializer):
    """
    Serializer for the user authentication object
    """
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )
        if not user:
            msg = ('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs


