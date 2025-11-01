from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'price', 'material', 'approved', 'stock', 'has_sustainability_info', 'created_at')
    list_filter = ('approved', 'created_at', 'material')
    search_fields = ('name', 'seller__brand_name', 'material', 'certifications')
    actions = ['approve_products', 'reject_products']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('seller', 'name', 'description', 'price', 'material', 'image', 'stock', 'approved')
        }),
        ('Sustainability Details', {
            'fields': ('raw_material_source', 'transportation_method', 'manufacturing_process', 'certifications'),
            'classes': ('collapse',),
        }),
        ('Environmental Impact', {
            'fields': ('carbon_footprint', 'water_usage', 'recyclability'),
            'classes': ('collapse',),
        }),
        ('Benefits & Impact', {
            'fields': ('environmental_benefits', 'usage_advantages', 'conventional_impact'),
            'classes': ('collapse',),
        }),
    )
    
    def has_sustainability_info(self, obj):
        return bool(obj.raw_material_source or obj.environmental_benefits or obj.manufacturing_process)
    has_sustainability_info.boolean = True
    has_sustainability_info.short_description = 'Has Sustainability Info'
    
    def approve_products(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f"{queryset.count()} products approved successfully.")
    approve_products.short_description = "Approve selected products"
    
    def reject_products(self, request, queryset):
        queryset.update(approved=False)
        self.message_user(request, f"{queryset.count()} products rejected.")
    reject_products.short_description = "Reject selected products"
