# Generated by Django 3.0.7 on 2020-06-24 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_auto_20200623_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveldata',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]