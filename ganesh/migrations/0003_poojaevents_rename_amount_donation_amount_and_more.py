# Generated by Django 4.0.6 on 2022-07-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganesh', '0002_rename_function33_donation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poojaevents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gotram', models.CharField(max_length=500)),
                ('SurName', models.CharField(max_length=500)),
                ('Name', models.CharField(max_length=500)),
                ('SpouseName', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'ganesh_poojaevents',
            },
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='amount',
            new_name='Amount',
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='child1',
            new_name='Child1',
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='child2',
            new_name='Child2',
        ),
        migrations.AlterModelTable(
            name='donation',
            table='ganesh_donation',
        ),
    ]
