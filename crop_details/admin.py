from django.contrib import admin
from .models import Commodity_Type, Product_Variety
# Register your models here.

admin.site.site_header = 'CropsAnalysis'

class CropsAdmin(admin.ModelAdmin):
    list_display = ('commodity', 'unit', 'volume_in_kgs', 'values_in_ksh', 'date')

 

admin.site.register(Commodity_Type, CropsAdmin)
admin.site.register(Product_Variety)
