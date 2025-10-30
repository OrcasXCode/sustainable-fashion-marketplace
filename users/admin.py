from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, SellerProfile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'phone', 'address')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('role', 'phone', 'address')}),
    )


@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'user', 'verified', 'created_at')
    list_filter = ('verified', 'created_at')
    search_fields = ('brand_name', 'user__username')
    actions = ['approve_sellers', 'reject_sellers']
    
    def approve_sellers(self, request, queryset):
        queryset.update(verified=True)
        self.message_user(request, f"{queryset.count()} sellers approved successfully.")
    approve_sellers.short_description = "Approve selected sellers"
    
    def reject_sellers(self, request, queryset):
        queryset.update(verified=False)
        self.message_user(request, f"{queryset.count()} sellers rejected.")
    reject_sellers.short_description = "Reject selected sellers"
