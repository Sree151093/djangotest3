# Generated by Django 3.0.7 on 2020-06-22 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_academicdetails_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicdetails',
            name='UGperc',
        ),
        migrations.RemoveField(
            model_name='personaldetails',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='personaldetails',
            name='Name',
        ),
        migrations.AddField(
            model_name='academicdetails',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='question_text',
            field=models.CharField(default='Hi', max_length=200, verbose_name='Question'),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='Int Value'),
        ),
    ]
