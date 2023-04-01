from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        # Telling the serializer what model to use to create the serializer.
        model = Project
        # Telling the serializer what fields to include in the serialized data.
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        # Telling the serializer that the `created_at` field is read only.
        read_only_fields = ('created_at', )