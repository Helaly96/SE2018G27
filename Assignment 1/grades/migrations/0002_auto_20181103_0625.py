# Generated by Django 2.1.3 on 2018-11-03 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20181031_1906'),
        ('courses', '0001_initial'),
        ('grades', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Grades',
            new_name='Grade',
        ),
    ]
