from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Game(models.Model):
    
    user_id = models.OneToOneField(User,on_delete=models.CASCADE,null=False)
    current_level = models.IntegerField(null=False,default=1)
    size = models.IntegerField(null=True,default=1)
    flash = models.IntegerField(null=True,default=1000)
    numbers = models.IntegerField(null=True,default=5)

    def __str__(self):
        return self.user_id