# Generated by Django 3.0.5 on 2020-04-07 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20200407_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
