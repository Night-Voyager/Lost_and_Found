from rest_framework import serializers

from .models import Student
# from apps.objects.models import FindObject, FindOwner


class StudentSerializer(serializers.ModelSerializer):
    # find_objects = serializers.PrimaryKeyRelatedField(many=True, queryset=FindObject.objects.all())
    # find_owners = serializers.PrimaryKeyRelatedField(many=True, queryset=FindOwner.objects.all())

    class Meta:
        model = Student
        fields = '__all__'
