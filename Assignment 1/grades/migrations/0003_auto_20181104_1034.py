# Generated by Django 2.1.3 on 2018-11-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0002_auto_20181103_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
