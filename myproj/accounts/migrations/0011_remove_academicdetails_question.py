# Generated by Django 3.0.7 on 2020-06-22 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_academicdetails_ugperc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicdetails',
            name='question',
        ),
    ]