# Generated by Django 3.0.2 on 2020-03-30 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200330_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Disc',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
    ]
