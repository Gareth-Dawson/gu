# Generated by Django 2.1.10 on 2019-08-06 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0008_article_author_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author_feedback',
            new_name='editor_feedback',
        ),
    ]
