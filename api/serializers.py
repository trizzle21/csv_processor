from rest_framework import serializers


class JSONImportLogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)
    data = serializers.JSONField(read_only=True)
    