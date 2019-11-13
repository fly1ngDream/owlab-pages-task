from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Page, VersionsThread


class VersionsThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionsThread
        fields = ('id',)


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = (
            'id',
            'title',
            'text',
            'version',
            'versions_thread',
            'is_current',
        )
        read_only_fields = (
            'version',
            'versions_thread',
            'is_current',
        )

    def create(self, validated_data):
        return Page.objects.create(
            title=validated_data.get('title'),
            text=validated_data.get('text'),
            versions_thread=VersionsThread.objects.create(),
        )

    def update(self, instance, validated_data):
        return Page.objects.create(
            title=validated_data.get('title'),
            text=validated_data.get('text'),
            versions_thread=instance.versions_thread,
            version = round(instance.version + 0.1, 1)
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
