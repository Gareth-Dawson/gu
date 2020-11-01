# Generated by Django 3.0.10 on 2020-11-01 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0013_auto_20201101_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='target',
            name='tweet_notified',
        ),
        migrations.RemoveField(
            model_name='target',
            name='tweet_notified_solution',
        ),
        migrations.AddField(
            model_name='target',
            name='tweeted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='target',
            name='tweeted_solution',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
