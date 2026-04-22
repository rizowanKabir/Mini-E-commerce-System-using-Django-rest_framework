from django.contrib import admin
from .models import ProductModel,OrderModel,OrderItem

# Register your models here.

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock']
    search_fields = ['name','price']

admin.site.register(OrderModel)
admin.site.register(OrderItem)    
