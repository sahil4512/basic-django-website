# Generated by Django 3.0.5 on 2020-04-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='agents/')),
            ],
            options={
                'verbose_name': 'Agent',
            },
        ),
    ]
