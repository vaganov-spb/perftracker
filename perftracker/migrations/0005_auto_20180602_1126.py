# Generated by Django 2.0.3 on 2018-06-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0004_auto_20180602_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='comparisonmodel',
            name='deleted',
            field=models.NullBooleanField(db_index=True, help_text='True means the Comparison was deleted'),
        ),
        migrations.AddField(
            model_name='jobmodel',
            name='deleted',
            field=models.NullBooleanField(db_index=True, help_text='True means the Job was deleted'),
        ),
    ]
