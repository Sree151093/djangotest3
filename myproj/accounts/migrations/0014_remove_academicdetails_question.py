# Generated by Django 3.0.7 on 2020-06-22 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_academicdetails_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicdetails',
            name='question',
        ),
    ]
