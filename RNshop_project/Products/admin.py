from django.contrib import admin
from .models import Product, Category 

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug':('name',)}




class ProductAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'price', 'added_on','produced_by','availability')

    list_editable = ('availability', 'price')
    
    list_filter = ('availability','produced_by')

    prepopulated_fields = {'slug':('name',)}



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


