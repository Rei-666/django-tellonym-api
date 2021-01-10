# Generated by Django 3.1.5 on 2021-01-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tellonym_api', '0005_remove_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='user',
            name='hashed_token',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
