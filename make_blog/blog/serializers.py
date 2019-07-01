from rest_framework import serializers
class CategorySerializer(serializers.Serializer):
    title = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

class NewsSerializer(serializers.Serializer):
    category = serializers.CharField()
    title = serializers.CharField()
    summary = serializers.CharField()
    content = serializers.CharField()
    image = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
