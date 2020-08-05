from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Computation(models.Model):
    comp = models.CharField(max_length=30)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.comp
