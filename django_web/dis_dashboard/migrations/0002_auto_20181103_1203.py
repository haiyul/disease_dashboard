# Generated by Django 2.1.1 on 2018-11-03 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dis_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aggcode',
            name='agg_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='discode',
            name='dis_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='gdcode',
            name='gd_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='monthcode',
            name='month',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
