from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", 'post', 'comments']


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ["__all__"]

class ProjetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ["__all__"]
        