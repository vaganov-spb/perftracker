# Generated by Django 2.0.3 on 2018-10-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0043_auto_20181005_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='hwfarmnodelocktypemodel',
            name='order',
            field=models.IntegerField(default=1, help_text='Priority in the list'),
        ),
    ]
