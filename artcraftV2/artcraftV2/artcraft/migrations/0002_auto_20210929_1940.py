# Generated by Django 3.2.7 on 2021-09-29 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artcraft', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='artist',
            table='artist',
        ),
        migrations.AlterModelTable(
            name='artwork',
            table='artwork',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
        migrations.AlterModelTable(
            name='order',
            table='order',
        ),
    ]
