# Generated by Django 4.2.3 on 2023-08-09 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_booking_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='car',
            field=models.TextField(),
        ),
    ]
