# Generated by Django 2.1.1 on 2018-11-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dis_dashboard', '0009_auto_20181105_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provinceborder',
            name='reg_id',
            field=models.ForeignKey(on_delete='SET_NULL', to='dis_dashboard.RegCode', to_field='reg_id'),
        ),
    ]