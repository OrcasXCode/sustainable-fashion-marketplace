from django.db import models
from django.conf import settings
from users.models import SellerProfile


class Product(models.Model):
    """Product listings by sellers"""
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=255, help_text="e.g., Organic Cotton, Recycled Polyester")
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    approved = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} by {self.seller.brand_name}"
