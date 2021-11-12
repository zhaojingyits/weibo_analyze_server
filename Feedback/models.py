from django.db import models

# Create your models here.
class FeedbackEntity(models.Model):
    id = models.AutoField(primary_key=True)
    app_user_id=models.CharField(max_length=30)
    wb_user_id=models.CharField(max_length=30)
    user_customize_score=models.IntegerField(default = 0)
    info=models.TextField(null=True)