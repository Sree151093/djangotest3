# Generated by Django 3.0.7 on 2020-06-22 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200621_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
    ]
