from django.db import models


<<<<<<< HEAD
class AggTb(models.Model):
    year = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    # month = models.ForeignKey('MonthCode', to_field='month', on_delete="SET_NULL")
    reg_id = models.CharField(max_length=50)
    dis_id = models.CharField(max_length=50)
    agg_id = models.CharField(max_length=50)
    gd_id = models.CharField(max_length=50)
=======
class InfDis(models.Model):
    area_name = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    month = models.CharField(max_length=10)
    dis_name = models.CharField(max_length=60)
>>>>>>> parent of 3e4d0c1... 刚导入数据库备份
    case_num = models.IntegerField()
    death_num = models.IntegerField()
    ici_rate = models.FloatField()
    mort_rate = models.FloatField()


<<<<<<< HEAD
class ProTb(models.Model):
    year = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    reg_id = models.CharField(max_length=50)
    dis_name = models.CharField(max_length=50)
    pro_name = models.CharField(max_length=50)
    case_num = models.IntegerField()
    dea_num = models.IntegerField()
    inci_rate = models.DecimalField(max_digits=10, decimal_places=4)
    mort_rate = models.DecimalField(max_digits=10, decimal_places=4)



class RegTb(models.Model):
    year = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    reg_id = models.CharField(max_length=50)
    disease = models.CharField(max_length=50)
    case_num = models.IntegerField()
    dea_num = models.IntegerField()
    inci_rate = models.DecimalField(max_digits=10, decimal_places=4)
    mort_rate = models.DecimalField(max_digits=10, decimal_places=4)


class AggCode(models.Model):
    agg_id = models.CharField(max_length=50)
    ag_g = models.CharField(max_length=50)


class DisCode(models.Model):
    dis_id = models.CharField(max_length=50)
    dis_name = models.CharField(max_length=50)


class GdCode(models.Model):
    gd_id = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)


class MonthCode(models.Model):
    month = models.CharField(max_length=50, unique=True)
    month_cn = models.CharField(max_length=50)


class ProCode(models.Model):
    pro_name = models.CharField(max_length=50)
    pro_id = models.CharField(max_length=50)

=======
class AreaList(models.Model):
    area_name = models.CharField(max_length=10)
    area_name_reg = models.CharField(max_length=10)
    area_name_short = models.CharField(max_length=10)
>>>>>>> parent of 3e4d0c1... 刚导入数据库备份


class DisList(models.Model):
    dis_name = models.CharField(max_length=60)
