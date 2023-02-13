from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields if field.name != "id"]
    search_fields = ('name', )

class CityAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(City, CityAdmin)
