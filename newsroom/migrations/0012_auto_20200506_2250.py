# Generated by Django 2.2.9 on 2020-05-06 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0011_auto_20200506_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='facebook_wait_time',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Minimum number of minutes after publication till post.', null=True),
        ),
    ]
