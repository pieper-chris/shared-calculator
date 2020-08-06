from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Computation(models.Model):
    comp = models.TextField(max_length=30,default=None,blank=True,null=True)
    entered_at = models.DateTimeField(default=datetime.now, blank=True)
