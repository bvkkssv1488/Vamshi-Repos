# Generated by Django 4.0.6 on 2022-07-23 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganesh', '0003_poojaevents_rename_amount_donation_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='poojaevents',
            name='Date',
            field=models.DateField(auto_now=True),
        ),
    ]
