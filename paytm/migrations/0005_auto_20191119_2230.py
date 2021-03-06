# Generated by Django 2.2.7 on 2019-11-19 22:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paytm', '0004_auto_20191119_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='playersinfo',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playersinfo',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
