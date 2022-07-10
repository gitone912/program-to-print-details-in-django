from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user(models.Model):
    firstname=models.CharField( max_length=50)
    lastname=models.CharField( max_length=50)
    age_inYears=models.IntegerField(blank=True,null=True)
    location=models.CharField( max_length=50)
      
    def __str__(self) -> str:
        return str(self.firstname)