# Generated by Django 2.1.1 on 2018-11-03 03:53

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
            model_name='aggtb',
            name='reg_id',
            field=models.ForeignKey(on_delete='SET_NULL', to='dis_dashboard.RegCode', to_field='reg_id'),
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
        migrations.AlterField(
            model_name='procode',
            name='pro_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='regcode',
            name='reg_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
