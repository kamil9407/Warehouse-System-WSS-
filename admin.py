from django.contrib import admin

from .models import Warehouse, WarehouseLocation, AddWare


# Register your models here.

admin.site.register(Warehouse)
admin.site.register(WarehouseLocation)
admin.site.register(AddWare)


