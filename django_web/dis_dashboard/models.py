from django.db import models


class InfDis(models.Model):
    area_name = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    month = models.CharField(max_length=10)
    dis_name = models.CharField(max_length=60)
    case_num = models.IntegerField()
    death_num = models.IntegerField()
    ici_rate = models.FloatField()
    mort_rate = models.FloatField()


class AreaList(models.Model):
    area_name = models.CharField(max_length=10)
    area_name_reg = models.CharField(max_length=10)
    area_name_short = models.CharField(max_length=10)


class DisList(models.Model):
    dis_name = models.CharField(max_length=60)
