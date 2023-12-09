from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from case.models import Case
from case.serializers import CaseSerializer
from case.utils import CaseAssigned
from authentication.models import User

import random

class CaseViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        queryset = Case.objects.all()
        serializer = CaseSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Case.objects.all()
        case = get_object_or_404(queryset, pk=pk)
        serializer = CaseSerializer(case)
        return Response(serializer.data)
    
    def create(self, request):
        request_data = {
            'category': request.data.get('category'),
            'documents': request.data.get('documents'),
            'type': request.data.get('type'),
            'created_by': request.user.id,
        }
        
        case_manager = User.objects.filter(roles='case_manager')
        case_manager = random.choice(case_manager)
        
        request_data['caseid'] = str(random.randint(111,999))+"/"+str(request.user.first_name)
        request_data['case_manager'] = case_manager.id
        
        serializer = CaseSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        CaseAssigned(request.user, case_manager, request_data['caseid'])
        
        return Response(serializer.data)