# Generated by Django 4.0.6 on 2022-08-18 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_remove_physicaldetail_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagedetails',
            name='status',
        ),
    ]