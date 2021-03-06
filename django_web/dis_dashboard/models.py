from django.contrib.gis.db import models


class AggTb(models.Model):
    year = models.CharField(max_length=50)
    month = models.ForeignKey("MonthCode", to_field="month", on_delete="SET_NULL")
    reg_id = models.ForeignKey("RegCode", to_field="reg_id", on_delete="SET_NULL")
    dis_id = models.ForeignKey("DisCode", to_field="dis_id", on_delete="SET_NULL")
    agg_id = models.ForeignKey("AggCode", to_field="agg_id", on_delete="SET_NULL")
    gd_id = models.ForeignKey("GdCode", to_field="gd_id", on_delete="SET_NULL")
    case_num = models.IntegerField()
    dea_num = models.IntegerField()
    inci_rate = models.DecimalField(max_digits=10, decimal_places=4)
    mort_rate = models.DecimalField(max_digits=10, decimal_places=4)


class ProTb(models.Model):
    year = models.CharField(max_length=50)
    month = models.ForeignKey("MonthCode", to_field="month", on_delete="SET_NULL")
    reg_id = models.ForeignKey("RegCode", to_field="reg_id", on_delete="SET_NULL")
    dis_id = models.ForeignKey("DisCode", to_field="dis_id", on_delete="SET_NULL")
    pro_name = models.ForeignKey("ProCode", to_field="pro_name", on_delete="SET_NULL")
    case_num = models.IntegerField()
    dea_num = models.IntegerField()
    inci_rate = models.DecimalField(max_digits=10, decimal_places=4)
    mort_rate = models.DecimalField(max_digits=10, decimal_places=4)


class RegTb(models.Model):
    year = models.CharField(max_length=50)
    month = models.ForeignKey("MonthCode", to_field="month", on_delete="SET_NULL")
    reg_id = models.ForeignKey("RegCode", to_field="reg_id", on_delete="SET_NULL")
    dis_id = models.ForeignKey("DisCode", to_field="dis_id", on_delete="SET_NULL")
    case_num = models.IntegerField()
    dea_num = models.IntegerField()
    inci_rate = models.DecimalField(max_digits=10, decimal_places=4)
    mort_rate = models.DecimalField(max_digits=10, decimal_places=4)


class AggCode(models.Model):
    agg_id = models.CharField(max_length=50, unique=True)
    ag_g = models.CharField(max_length=50)
    ag_g_ctr = models.CharField(max_length=50, default="null")
    ag_g_p5 = models.CharField(max_length=50, default="")


class DisCode(models.Model):
    dis_id = models.CharField(max_length=50, unique=True)
    dis_name = models.CharField(max_length=50)


class GdCode(models.Model):
    gd_id = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=50)


class MonthCode(models.Model):
    month = models.CharField(max_length=50, unique=True)
    month_cn = models.CharField(max_length=50)


class ProCode(models.Model):
    pro_name = models.CharField(max_length=50, unique=True)
    pro_id = models.CharField(max_length=50, unique=True)


class RegCode(models.Model):
    reg_id = models.CharField(max_length=50, unique=True)
    reg_name = models.CharField(max_length=50)
    reg_name_crt = models.CharField(max_length=50, default="null")
    admin_id = models.CharField(max_length=50, default="")


class ProvinceBorder(models.Model):
    name = models.CharField(max_length=24)
    popname = models.CharField(max_length=24)
    code = models.CharField(max_length=12)
    type = models.BigIntegerField()
    display = models.BigIntegerField()
    x = models.FloatField()
    y = models.FloatField()
    py = models.CharField(max_length=50)
    geom = models.PolygonField(srid=4326)
    reg_id = models.ForeignKey("RegCode", to_field="reg_id", on_delete="SET_NULL")



