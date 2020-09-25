from django.contrib.auth.models import User
from django.db import models
# from datetime import datetime

class Computation(models.Model):
    comp = models.TextField(max_length=30,default=None,blank=True,null=True)
    '''t = datetime.now()
    s = t.strftime("%c %Z")'''
    entered_at = models.TextField(max_length=30,default=None,blank=True,null=True)
    # entered_at = models.DateTimeField(default=s, blank=True)
    
    def __str__(self):
        return self.comp
