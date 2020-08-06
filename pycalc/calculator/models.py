from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from datetime import datetime

class Computation(models.Model):
    comp = models.TextField(max_length=30,default=None,blank=True,null=True)
    entered_at = models.DateTimeField(default=datetime.now, blank=True)
    #created_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.DO_NOTHING)
    
    #def __str__(self):
        #return self.comp
