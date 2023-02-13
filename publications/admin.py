from django.contrib import admin

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields if field.name != "id"]
    search_fields = ('name', )

class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields if field.name != "id"]
    search_fields = ('name', 'author',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)