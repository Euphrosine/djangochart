# Generated by Django 4.2.5 on 2023-10-04 11:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='status',
            field=models.IntegerField(default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
    ]
