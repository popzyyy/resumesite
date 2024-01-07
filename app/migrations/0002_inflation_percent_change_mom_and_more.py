# Generated by Django 4.2.8 on 2023-12-21 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inflation',
            name='percent_change_mom',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=25, null=True),
        ),
        migrations.AddField(
            model_name='inflation',
            name='percent_change_yom',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=25, null=True),
        ),
    ]
