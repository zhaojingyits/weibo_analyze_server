# Generated by Django 2.2 on 2020-05-05 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiboEntity', '0004_auto_20200505_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='weibo',
            name='at_users',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='weibo',
            name='pics',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='weibo',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='weibo',
            name='video_url',
            field=models.TextField(default=''),
        ),
    ]