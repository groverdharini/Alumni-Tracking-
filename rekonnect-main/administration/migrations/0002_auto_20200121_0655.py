# Generated by Django 2.2.5 on 2020-01-21 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_userinfo',
            name='stud_username',
        ),
        migrations.AddField(
            model_name='admin_userinfo',
            name='stud_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
