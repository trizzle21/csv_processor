from rest_framework import serializers
from api.models import

class CSVImportRecordSerializer(serializers.Serializer):
    
    class Meta:
        model = CSVImportRecord
        fields = ('created', 'modified', 'customer', 'errors')
