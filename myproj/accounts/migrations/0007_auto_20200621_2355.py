# Generated by Django 3.0.7 on 2020-06-22 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200621_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='Name',
            field=models.CharField(default='', max_length=50, verbose_name='Full Name'),
        ),
    ]