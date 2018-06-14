from rest_framework import serializers


class CSVImportRecordSerializer(serializers.Serializer):
    
    class Meta:
        model = CSVImportRecord
        fields = ('created', 'modified', 'customer', 'errors')
    