# Generated by Django 5.1.2 on 2024-10-19 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Int', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='file',
        ),
    ]
