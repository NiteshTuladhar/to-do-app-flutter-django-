# Generated by Django 3.0.7 on 2021-01-14 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='discription',
            new_name='description',
        ),
    ]
