# Generated by Django 3.0.6 on 2020-05-13 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0005_auto_20200513_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objfile',
            name='task',
        ),
    ]