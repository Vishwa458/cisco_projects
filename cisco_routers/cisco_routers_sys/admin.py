from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import *


@admin.register(Routers)
class ViewAdmin(ImportExportModelAdmin):
    pass
