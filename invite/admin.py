from django.contrib import admin
from .models import *


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'id']
    list_display_links = ['name', 'last_name', 'id']


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'price', 'id']
    list_display_links = ['title', 'price']


admin.site.register(Person, PersonAdmin)
admin.site.register(Goods, GoodsAdmin)
