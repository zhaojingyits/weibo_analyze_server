# Generated by Django 2.2 on 2020-05-05 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiboEntity', '0010_auto_20200505_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weibo',
            name='created_at',
            field=models.DateField(null=True),
        ),
    ]
