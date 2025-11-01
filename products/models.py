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
    
    # Detailed Sustainability Information
    raw_material_source = models.TextField(
        blank=True,
        help_text="Where the raw materials come from (origin, farms, suppliers)"
    )
    transportation_method = models.TextField(
        blank=True,
        help_text="How raw materials are transported (carbon footprint, shipping methods)"
    )
    manufacturing_process = models.TextField(
        blank=True,
        help_text="Detailed process of how the product is made"
    )
    certifications = models.CharField(
        max_length=500,
        blank=True,
        help_text="e.g., GOTS, Fair Trade, OEKO-TEX, etc."
    )
    environmental_benefits = models.TextField(
        blank=True,
        help_text="Benefits of using this sustainable product"
    )
    usage_advantages = models.TextField(
        blank=True,
        help_text="Why consumers should choose this product"
    )
    conventional_impact = models.TextField(
        blank=True,
        help_text="Environmental impact of NOT using sustainable alternatives"
    )
    carbon_footprint = models.CharField(
        max_length=255,
        blank=True,
        help_text="Carbon footprint information (e.g., kg CO2 saved)"
    )
    water_usage = models.CharField(
        max_length=255,
        blank=True,
        help_text="Water consumption in production"
    )
    recyclability = models.CharField(
        max_length=255,
        blank=True,
        help_text="How the product can be recycled or disposed"
    )
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} by {self.seller.brand_name}"
