# Generated by Django 3.0.10 on 2021-02-23 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_auto_20210222_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='split',
            field=models.BooleanField(default=False),
        ),
    ]
