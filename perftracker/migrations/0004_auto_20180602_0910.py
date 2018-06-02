# Generated by Django 2.0.3 on 2018-06-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0003_testmodel_samples'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='avg_plusmin',
            field=models.FloatField(null=True, verbose_name='Deviation in % of average score: 0.02'),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='max_plusmin',
            field=models.FloatField(null=True, verbose_name='Deviation in % of max score: 0.03'),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='min_plusmin',
            field=models.FloatField(null=True, verbose_name='Deviation in % of min score: 0.01'),
        ),
    ]
