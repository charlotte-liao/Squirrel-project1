# Generated by Django 3.1.2 on 2020-10-22 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SquirrelApp', '0011_auto_20201022_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='Age',
            field=models.CharField(blank='True', default=0, help_text='Age', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Shift',
            field=models.CharField(blank='True', choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', help_text='Shift', max_length=20, null=True),
        ),
    ]
