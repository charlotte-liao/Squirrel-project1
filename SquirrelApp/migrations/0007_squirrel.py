# Generated by Django 3.1.2 on 2020-10-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SquirrelApp', '0006_auto_20201016_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('UniqueSquirrelID', models.CharField(help_text='Unique Squirrel ID', max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]