# Generated by Django 2.1.1 on 2018-11-03 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dis_dashboard', '0002_auto_20181103_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aggtb',
            name='month',
            field=models.ForeignKey(on_delete='SET_NULL', to='dis_dashboard.MonthCode', to_field='month'),
        ),
    ]
