# Generated by Django 3.0.2 on 2020-04-03 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='category',
            new_name='Email',
        ),
    ]
