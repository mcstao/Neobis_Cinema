# Generated by Django 4.2.7 on 2023-11-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0016_alter_ticket_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
    ]
