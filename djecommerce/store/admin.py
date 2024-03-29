from django.contrib import admin

from .models import Category,Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'slug'] #model fields
    #whatever the name we enter for the name it will be prepopulated in the slug field
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'author', 'slug','price', 'in_stock', 'created', 'updated']
    #To create a list filter for these fields
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    #whatever the title we enter for the name it will be prepopulated in the slug field
    prepopulated_fields = {'slug': ('title',)}
