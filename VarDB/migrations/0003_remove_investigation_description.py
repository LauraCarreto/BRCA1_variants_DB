# Generated by Django 2.0.2 on 2018-03-01 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VarDB', '0002_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investigation',
            name='description',
        ),
    ]