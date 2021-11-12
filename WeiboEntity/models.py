from django.db import models

# Create your models here.
class Weibo(models.Model):
    id=models.CharField(max_length=20,primary_key=True)
    bid=models.CharField(max_length=12)
    user_id=models.CharField(max_length=20)
    screen_name=models.CharField(max_length=30)
    text=models.TextField(null=True)
    topics=models.CharField(max_length=200)
    at_users=models.TextField(null=True)
    pics=models.TextField(null=True)
    video_url=models.TextField(null=True)
    location=models.CharField(max_length=100)
    created_at=models.DateField(null=True)
    source=models.CharField(max_length=30)
    attitudes_count=models.IntegerField(default = 0)
    comments_count=models.IntegerField(default = 0)
    reposts_count=models.IntegerField(default = 0)
    retweet_id=models.CharField(max_length=20)