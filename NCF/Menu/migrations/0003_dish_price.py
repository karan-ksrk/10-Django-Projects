# Generated by Django 3.1.2 on 2020-10-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0002_auto_20201009_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='Price',
            field=models.IntegerField(default=0),
        ),
    ]
