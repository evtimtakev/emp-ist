# Generated by Django 2.2.6 on 2019-10-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191017_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='project_start_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
