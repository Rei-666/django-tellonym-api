# Generated by Django 3.1.5 on 2021-01-09 12:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tellonym_api', '0006_auto_20210109_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tellonym',
            name='state',
            field=models.CharField(choices=[('NEW', 'Nowy'), ('ACCEPTED', 'Pobrany'), ('DISCARDED', 'Odrzucony')], default='NEW', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
