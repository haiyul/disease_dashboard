from django.db import models


class AggTb(models.Model):
    year = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    # month = models.ForeignKey('MonthCode', to_field='month', on_delete="SET_NULL")
    reg_id = models.CharField(max_length=50)
    dis_id = models.CharField(max_length=50)
    agg_id = models.CharField(max_length=50)
    gd_id = models.CharField(max_length=50)
    case_num = models.IntegerField()
    dea_num = models.IntegerField()
    inci_rate = models.DecimalField(max_digits=10, decimal_places=4)
    mort_rate = models.DecimalField(max_digits=10, decimal_places=4)


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


class RegCode(models.Model):
    reg_id = models.CharField(max_length=50)
    reg_name = models.CharField(max_length=50)

