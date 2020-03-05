from django.contrib import admin
from .models import Property, Category, Area

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_on')
    list_filter = ('category', 'created_on')
    search_fields = ('name',)



admin.site.register(Property, PropertyAdmin)
admin.site.register(Category)
admin.site.register(Area)
