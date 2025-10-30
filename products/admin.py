from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'price', 'material', 'approved', 'stock', 'created_at')
    list_filter = ('approved', 'created_at', 'material')
    search_fields = ('name', 'seller__brand_name', 'material')
    actions = ['approve_products', 'reject_products']
    
    def approve_products(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f"{queryset.count()} products approved successfully.")
    approve_products.short_description = "Approve selected products"
    
    def reject_products(self, request, queryset):
        queryset.update(approved=False)
        self.message_user(request, f"{queryset.count()} products rejected.")
    reject_products.short_description = "Reject selected products"
