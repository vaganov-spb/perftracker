# Generated by Django 2.1.5 on 2019-10-14 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0052_jobmodel_recalc_errors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmodel',
            name='testcases_errors',
            field=models.IntegerField(help_text='Number of test cases with test errors/failures'),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='testcases_total',
            field=models.IntegerField(help_text='Total number of test cases in the job'),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='tests_completed',
            field=models.IntegerField(help_text='Number of tests completed'),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='tests_errors',
            field=models.IntegerField(default=0, help_text='Number of tests with errors (includes failed)'),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='tests_failed',
            field=models.IntegerField(default=0, help_text='Number of failed tests'),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='tests_total',
            field=models.IntegerField(help_text='Total number of tests in the job'),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='tests_warnings',
            field=models.IntegerField(default=0, help_text='Number of tests with warnings'),
        ),
    ]
