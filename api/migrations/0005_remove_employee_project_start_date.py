# Generated by Django 2.2.6 on 2019-10-17 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191017_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='project_start_date',
        ),
    ]