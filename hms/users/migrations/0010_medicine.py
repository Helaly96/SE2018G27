# Generated by Django 2.1.3 on 2019-02-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_report_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, null=True)),
                ('provider', models.CharField(max_length=30, null=True)),
                ('quantity', models.IntegerField(null=True)),
            ],
        ),
    ]
