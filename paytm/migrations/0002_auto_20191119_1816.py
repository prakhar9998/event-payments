# Generated by Django 2.2.7 on 2019-11-19 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paytm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_status',
        ),
        migrations.AddField(
            model_name='playersinfo',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]