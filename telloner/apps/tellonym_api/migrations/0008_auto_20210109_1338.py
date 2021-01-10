# Generated by Django 3.1.5 on 2021-01-09 12:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tellonym_api', '0007_auto_20210109_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tellonym',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
