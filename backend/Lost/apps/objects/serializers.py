from rest_framework import serializers

from .models import FindObject, FindOwner


class FindObjectSerializer(serializers.ModelSerializer):
    # publisher = serializers.ReadOnlyField(source='publisher.name')

    class Meta:
        model = FindObject
        fields = '__all__'


class FindOwnerSerializer(serializers.ModelSerializer):
    # publisher = serializers.ReadOnlyField(source='publisher.name')

    class Meta:
        model = FindOwner
        fields = '__all__'
