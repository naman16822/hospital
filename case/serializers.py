from rest_framework import serializers

from case.models import Case

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['id', 'caseid', 'created_by', 'created_at', 'case_manager', 'category', 'documents', 'type', ]
