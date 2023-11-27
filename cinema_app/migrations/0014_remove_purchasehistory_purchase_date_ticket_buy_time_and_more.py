# Generated by Django 4.2.7 on 2023-11-27 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0013_alter_purchasehistory_movies_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasehistory',
            name='purchase_date',
        ),
        migrations.AddField(
            model_name='ticket',
            name='buy_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
