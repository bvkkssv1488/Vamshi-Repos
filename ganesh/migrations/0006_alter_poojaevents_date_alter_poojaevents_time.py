# Generated by Django 4.0.6 on 2022-07-24 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganesh', '0005_poojaevents_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poojaevents',
            name='Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='poojaevents',
            name='Time',
            field=models.CharField(default='Morning', max_length=500),
        ),
    ]