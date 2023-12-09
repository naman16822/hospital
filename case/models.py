from django.db import models

from authentication.models import User

class Case(models.Model):
    TYPE = (
        ('new', 'New'),
        ('follow-up', 'Follow-UP')
    )
    caseid = models.CharField(max_length=30)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    created_at = models.DateTimeField(auto_now_add=True)
    case_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='case_manager', null=True, blank=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    documents = models.FileField(upload_to='media/case/documents/', blank=True, null=True)
    type = models.CharField(max_length=30, choices=TYPE, default='new')
    
    def __str__(self):
        return f'{self.created_by.username} - {self.caseid}'
