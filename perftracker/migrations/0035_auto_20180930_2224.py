# Generated by Django 2.0.3 on 2018-09-30 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0034_auto_20180930_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artifactmetamodel',
            old_name='gc_dt',
            new_name='expires_dt',
        ),
    ]
