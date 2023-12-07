from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('patient', 'Patient'),
        ('case_manager', 'Case Manager')
    )
    
    roles = models.CharField(max_length=20, choices=ROLES, default='patient')
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        db_table = "Users"
        verbose_name = 'User'
        
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
