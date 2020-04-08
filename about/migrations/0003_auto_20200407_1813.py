# Generated by Django 3.0.5 on 2020-04-07 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20200406_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='about/%Y/%m/%d'),
        ),
    ]