# users/models.py
from django.contrib.auth.models import User
from django.db import models

class CustomUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True,related_name='custom_user')
    current_score  = models.IntegerField(null=True,default=0)
    high_score  = models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.user.username
    
    