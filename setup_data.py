"""
Script to set admin password and create sample data
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sustainable_fashion.settings')
django.setup()

from django.contrib.auth import get_user_model
from users.models import SellerProfile
from products.models import Product

User = get_user_model()

# Set admin password
admin = User.objects.get(username='admin')
admin.set_password('admin123')
admin.role = 'admin'
admin.is_staff = True
admin.is_superuser = True
admin.save()
print("✓ Admin password set to: admin123")

# Create a sample buyer
buyer, created = User.objects.get_or_create(
    username='buyer1',
    defaults={
        'email': 'buyer@example.com',
        'role': 'buyer',
        'phone': '123-456-7890',
        'address': '123 Main St, City, State 12345'
    }
)
if created:
    buyer.set_password('buyer123')
    buyer.save()
    print("✓ Sample buyer created - Username: buyer1, Password: buyer123")

# Create sample sellers
sellers_data = [
    {
        'username': 'eco_threads',
        'email': 'contact@ecothreads.com',
        'brand_name': 'EcoThreads',
        'description': 'Sustainable fashion made from organic cotton and recycled materials.',
        'verified': True
    },
    {
        'username': 'green_wear',
        'email': 'hello@greenwear.com',
        'brand_name': 'GreenWear',
        'description': 'Ethical fashion brand focused on fair trade and eco-friendly production.',
        'verified': True
    },
]

for seller_data in sellers_data:
    user, created = User.objects.get_or_create(
        username=seller_data['username'],
        defaults={
            'email': seller_data['email'],
            'role': 'seller',
        }
    )
    if created:
        user.set_password('seller123')
        user.save()
        
        SellerProfile.objects.create(
            user=user,
            brand_name=seller_data['brand_name'],
            description=seller_data['description'],
            verified=seller_data['verified']
        )
        print(f"✓ Seller created - Brand: {seller_data['brand_name']}, Username: {seller_data['username']}, Password: seller123")

# Create sample products
products_data = [
    {
        'seller': 'eco_threads',
        'name': 'Organic Cotton T-Shirt',
        'description': 'Classic crew neck t-shirt made from 100% organic cotton. Soft, breathable, and environmentally friendly.',
        'price': 2499,
        'material': 'Organic Cotton',
        'stock': 50,
        'approved': True
    },
    {
        'seller': 'eco_threads',
        'name': 'Recycled Denim Jeans',
        'description': 'Stylish jeans crafted from recycled denim. Comfortable fit with a sustainable conscience.',
        'price': 6499,
        'material': 'Recycled Denim',
        'stock': 30,
        'approved': True
    },
    {
        'seller': 'green_wear',
        'name': 'Hemp Blend Hoodie',
        'description': 'Cozy hoodie made from hemp and organic cotton blend. Perfect for casual wear.',
        'price': 5499,
        'material': 'Hemp & Organic Cotton',
        'stock': 40,
        'approved': True
    },
    {
        'seller': 'green_wear',
        'name': 'Bamboo Fiber Dress',
        'description': 'Elegant dress made from sustainable bamboo fiber. Lightweight and breathable.',
        'price': 7499,
        'material': 'Bamboo Fiber',
        'stock': 25,
        'approved': True
    },
    {
        'seller': 'eco_threads',
        'name': 'Recycled Polyester Jacket',
        'description': 'Water-resistant jacket made from recycled plastic bottles. Stylish and sustainable.',
        'price': 10999,
        'material': 'Recycled Polyester',
        'stock': 20,
        'approved': True
    },
    {
        'seller': 'green_wear',
        'name': 'Organic Linen Shirt',
        'description': 'Breathable linen shirt perfect for summer. Made from certified organic linen.',
        'price': 4599,
        'material': 'Organic Linen',
        'stock': 35,
        'approved': True
    },
]

for product_data in products_data:
    seller_user = User.objects.get(username=product_data['seller'])
    seller_profile = seller_user.seller_profile
    
    product, created = Product.objects.get_or_create(
        seller=seller_profile,
        name=product_data['name'],
        defaults={
            'description': product_data['description'],
            'price': product_data['price'],
            'material': product_data['material'],
            'stock': product_data['stock'],
            'approved': product_data['approved']
        }
    )
    if created:
        print(f"✓ Product created: {product_data['name']}")

print("\n" + "="*60)
print("SETUP COMPLETE!")
print("="*60)
print("\nYou can now login with:")
print("  Admin:  username: admin,      password: admin123")
print("  Buyer:  username: buyer1,     password: buyer123")
print("  Seller: username: eco_threads or green_wear, password: seller123")
print("\nRun the server: python manage.py runserver")
print("="*60)
