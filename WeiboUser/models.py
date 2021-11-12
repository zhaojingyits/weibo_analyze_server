from django.db import models

# Create your models here.
class User(models.Model):
    id=models.CharField(max_length=20,primary_key=True)
    screen_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    statuses_count=models.IntegerField(default = 0)
    followers_count=models.IntegerField(default = 0)
    follow_count=models.IntegerField(default = 0)
    registration_time=models.CharField(max_length=20)
    sunshine=models.CharField(max_length=20)
    birthday=models.CharField(max_length=40)
    location=models.CharField(max_length=200)
    education=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    description=models.CharField(max_length=140)
    profile_url=models.CharField(max_length=200)
    profile_image_url=models.CharField(max_length=200)
    avatar_hd=models.CharField(max_length=200)
    urank=models.IntegerField(default = 0)
    mbrank=models.IntegerField(default = 0)
    verified=models.BooleanField(default=False)
    verified_type=models.IntegerField(default = 0)
    verified_reason=models.CharField(max_length=140)