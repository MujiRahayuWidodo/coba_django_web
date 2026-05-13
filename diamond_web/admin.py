from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import DiamondItem

@admin.register(DiamondItem)
class DiamondItemAdmin(ImportExportModelAdmin):
    list_display = ('name', 'carat', 'price', 'stock', 'created_at')
    search_fields = ('name',)
    list_filter = ('stock', 'created_at')