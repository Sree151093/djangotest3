# Generated by Django 3.0.7 on 2020-06-22 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicdetails',
            name='Idea',
        ),
        migrations.AddField(
            model_name='academicdetails',
            name='UGperc',
            field=models.IntegerField(default=0, verbose_name='UnderGrad Percentage'),
        ),
    ]