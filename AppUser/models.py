from django.db import models

# Create your models here.
class AppUserInfo(models.Model):
    id=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=12)
    c_time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)