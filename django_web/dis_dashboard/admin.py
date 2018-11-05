from django.contrib.gis import admin as admin_gis
from django.contrib import admin
from .models import *

admin.site.register(ProvinceBorder, admin_gis.GeoModelAdmin)
# admin.site.register(excel_df_in)
# admin.site.register(excel_df_out)
# admin.site.register(csv_df_temp)
# admin.site.register(yaodian_all)
# admin.site.register(data_demo)



