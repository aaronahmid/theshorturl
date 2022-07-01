#!/usr/bin/env python
""" serializers
"""
from rest_framework import serializers
from shortener.models import ShortUrl


class ShortSerializer(serializers.Serializer):
    """ short serializer class
    """
    name = serializers.CharField(max_length=65, min_length=8)
    url = serializers.URLField(
        max_length=200, min_length=None, allow_blank=False)

    class Meta:
        """ Meta data
        """
        model = ShortUrl
        fields = '__all__'

    def validate(self, attrs):
        """ data validation
        """
        return super().validate(attrs)

    def create(self, validated_data):
        """ creates objects using the object model
        """
        return ShortUrl.objects.create(**validated_data)
