from django.contrib import admin
from main.models import Cereal, Manufacturer, Nutritionam_Facts
# Register your models here.

# class CerealAdmin(admin.ModelAdmin):
# 	'list_display' = ('name', 'manufacturer')
# 	search_field = ('name')

admin.site.register(Cereal)
admin.site.register(Manufacturer)
admin.site.register(Nutritionam_Facts)

