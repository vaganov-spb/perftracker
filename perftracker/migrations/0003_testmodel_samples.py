# Generated by Django 2.0.3 on 2018-05-04 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0002_comparisonmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='samples',
            field=models.IntegerField(default=1, help_text='Number of test samples (iterations)'),
        ),
    ]
