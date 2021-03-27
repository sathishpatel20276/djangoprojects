from django.contrib import admin
from fakeapp.models import FakeData
# Register your models here.

@admin.register(FakeData)
class FakeAdmin(admin.ModelAdmin):
    list_filter = ['first_name','job','company']