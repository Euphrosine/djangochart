# Generated by Django 4.2.5 on 2023-09-30 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('num_of_products', models.IntegerField()),
            ],
        ),
    ]