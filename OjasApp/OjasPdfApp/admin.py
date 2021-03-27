from django.contrib import admin
from .models import OjasPdfData
# Register your models here.

@admin.register(OjasPdfData)
class OjasPdf(admin.ModelAdmin):
    list_filter = ['title','pdf','cover']