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

# Create sample products with detailed sustainability information
products_data = [
    {
        'seller': 'eco_threads',
        'name': 'Organic Cotton T-Shirt',
        'description': 'Classic crew neck t-shirt made from 100% organic cotton. Soft, breathable, and environmentally friendly.',
        'price': 2499,
        'material': 'Organic Cotton',
        'stock': 50,
        'approved': True,
        'raw_material_source': 'Sourced from certified organic cotton farms in Maharashtra, India. Farmers use natural fertilizers and traditional farming methods without harmful pesticides.',
        'transportation_method': 'Raw cotton transported via local trains to reduce carbon emissions. Processing facility located within 100km of farms.',
        'manufacturing_process': 'Hand-picked cotton is processed using eco-friendly techniques. Dyed with natural plant-based colors. Manufacturing follows GOTS standards with zero chemical waste.',
        'certifications': 'GOTS, Fair Trade, OEKO-TEX Standard 100',
        'environmental_benefits': 'Uses 91% less water than conventional cotton. No toxic chemicals pollute waterways. Biodegradable fabric returns nutrients to soil.',
        'usage_advantages': 'Hypoallergenic and gentle on sensitive skin. Breathable fabric keeps you cool. Durability means longer product life and less waste.',
        'conventional_impact': 'Conventional cotton uses 16% of world\'s pesticides. These chemicals harm farmworkers, contaminate water sources, and destroy soil health over time.',
        'carbon_footprint': '2.1 kg CO₂ saved per garment',
        'water_usage': '95% less water than conventional cotton',
        'recyclability': '100% biodegradable, can be composted'
    },
    {
        'seller': 'eco_threads',
        'name': 'Recycled Denim Jeans',
        'description': 'Stylish jeans crafted from recycled denim. Comfortable fit with a sustainable conscience.',
        'price': 6499,
        'material': 'Recycled Denim',
        'stock': 30,
        'approved': True,
        'raw_material_source': 'Made from post-consumer denim waste collected from textile recycling centers across India. Each pair contains 65% recycled denim fibers.',
        'transportation_method': 'Collection centers strategically placed in major cities. Consolidated shipping reduces transport emissions by 40%.',
        'manufacturing_process': 'Old denim is mechanically shredded, re-spun into yarn, and woven. Water-saving washing techniques reduce water use by 80%. No stone washing or harsh chemicals.',
        'certifications': 'GRS (Global Recycled Standard), Cradle to Cradle',
        'environmental_benefits': 'Diverts textile waste from landfills. Reduces water pollution from denim manufacturing. Each pair saves equivalent of 1 year of drinking water.',
        'usage_advantages': 'Same durability as virgin denim with softer feel. Unique character from recycled fibers. Supports circular fashion economy.',
        'conventional_impact': 'Traditional denim production is water-intensive and uses toxic chemicals. 2,000 gallons of water needed per pair. Chemical runoff creates "dead zones" in rivers.',
        'carbon_footprint': '25 kg CO₂ saved per pair',
        'water_usage': '80% reduction (1,500 liters vs 8,000 liters)',
        'recyclability': 'Can be recycled again at end of life'
    },
    {
        'seller': 'green_wear',
        'name': 'Hemp Blend Hoodie',
        'description': 'Cozy hoodie made from hemp and organic cotton blend. Perfect for casual wear.',
        'price': 5499,
        'material': 'Hemp & Organic Cotton',
        'stock': 40,
        'approved': True,
        'raw_material_source': 'Hemp grown in Uttarakhand hills using regenerative agriculture. Organic cotton from Tamil Nadu. Both crops improve soil health naturally.',
        'transportation_method': 'Regional sourcing minimizes transport. Fibers processed at local mills powered by renewable energy.',
        'manufacturing_process': '55% hemp, 45% organic cotton blend. Natural retting process for hemp. Low-impact dyes. Solar-powered facility.',
        'certifications': 'Hemp Trade Association, USDA Organic',
        'environmental_benefits': 'Hemp absorbs 4x more CO₂ than trees. Requires no pesticides. Enriches soil for future crops. Naturally antimicrobial.',
        'usage_advantages': 'Gets softer with each wash. Naturally temperature regulating. Anti-microbial means fewer washes needed. Extremely durable.',
        'conventional_impact': 'Synthetic hoodies made from petroleum. Non-biodegradable microplastics pollute oceans. Energy-intensive production releases greenhouse gases.',
        'carbon_footprint': 'Carbon negative - absorbs 3.2 kg CO₂',
        'water_usage': 'Hemp needs 50% less water than cotton',
        'recyclability': 'Fully biodegradable natural fibers'
    },
    {
        'seller': 'green_wear',
        'name': 'Bamboo Fiber Dress',
        'description': 'Elegant dress made from sustainable bamboo fiber. Lightweight and breathable.',
        'price': 7499,
        'material': 'Bamboo Fiber',
        'stock': 25,
        'approved': True,
        'raw_material_source': 'Bamboo harvested from FSC-certified forests in Northeast India. Grows naturally without irrigation, pesticides, or fertilizers.',
        'transportation_method': 'Processing mill located adjacent to bamboo forests. Closed-loop production system recycles all water and solvents.',
        'manufacturing_process': 'Mechanical crushing (not chemical processing) preserves bamboo\'s natural properties. Lyocell process recycles 99.5% of solvents. Eco-friendly dyeing.',
        'certifications': 'FSC Certified, OEKO-TEX, Ecocert',
        'environmental_benefits': 'Bamboo grows 3 feet per day, fastest plant on earth. Produces 35% more oxygen than trees. Natural pest resistance means no pesticides.',
        'usage_advantages': 'Naturally moisture-wicking and breathable. UV protective. Hypoallergenic and antibacterial. Silky smooth texture.',
        'conventional_impact': 'Synthetic fabrics like polyester are made from fossil fuels. Release microplastics when washed. Take 200+ years to decompose in landfills.',
        'carbon_footprint': '5.4 kg CO₂ saved vs synthetic dress',
        'water_usage': 'Bamboo requires no irrigation',
        'recyclability': 'Biodegrades within 1 year'
    },
    {
        'seller': 'eco_threads',
        'name': 'Recycled Polyester Jacket',
        'description': 'Water-resistant jacket made from recycled plastic bottles. Stylish and sustainable.',
        'price': 10999,
        'material': 'Recycled Polyester',
        'stock': 20,
        'approved': True,
        'raw_material_source': 'Made from post-consumer PET bottles collected from Mumbai and Delhi recycling programs. Each jacket diverts 12 plastic bottles from oceans.',
        'transportation_method': 'Bottles collected through municipal programs. Transported to nearby recycling facility. Reduces virgin polyester shipping from overseas.',
        'manufacturing_process': 'Bottles cleaned, shredded into flakes, melted, and extruded into fibers. No new petroleum used. DWR coating is PFC-free and eco-friendly.',
        'certifications': 'GRS (Global Recycled Standard), bluesign approved',
        'environmental_benefits': 'Prevents plastic ocean pollution. Uses 59% less energy than virgin polyester. Reduces petroleum dependency. Each jacket = 12 bottles saved.',
        'usage_advantages': 'Same performance as virgin polyester. Water-resistant and durable. Easy care - machine washable. Lightweight and packable.',
        'conventional_impact': 'Virgin polyester production uses crude oil. Energy-intensive manufacturing. Plastic pollution kills marine life. Microplastics enter food chain.',
        'carbon_footprint': '7.8 kg CO₂ saved per jacket',
        'water_usage': '90% less water than virgin polyester',
        'recyclability': 'Can be recycled into new products'
    },
    {
        'seller': 'green_wear',
        'name': 'Organic Linen Shirt',
        'description': 'Breathable linen shirt perfect for summer. Made from certified organic linen.',
        'price': 4599,
        'material': 'Organic Linen',
        'stock': 35,
        'approved': True,
        'raw_material_source': 'Organic flax grown in Punjab without synthetic fertilizers. Flax is naturally pest-resistant and requires minimal water.',
        'transportation_method': 'Flax processed at local facility using traditional methods. Short supply chain reduces transport emissions.',
        'manufacturing_process': 'Traditional retting process uses natural bacteria. Mechanical processing without chemicals. Stone-washed for softness using minimal water.',
        'certifications': 'European Flax, GOTS, Made in Green',
        'environmental_benefits': 'Flax plant uses entire stalk - zero waste. Improves soil quality. Sequesters carbon. Uses 5x less water than cotton.',
        'usage_advantages': 'Natural temperature regulation keeps you cool. Gets softer over time. Highly breathable. Naturally anti-bacterial reduces odors.',
        'conventional_impact': 'Conventional cotton shirts require heavy pesticide use. Chemical processing pollutes water. Synthetic shirts shed microplastics with every wash.',
        'carbon_footprint': '1.8 kg CO₂ saved vs conventional shirt',
        'water_usage': '80% less than cotton production',
        'recyclability': '100% natural, fully biodegradable'
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
            'approved': product_data['approved'],
            'raw_material_source': product_data.get('raw_material_source', ''),
            'transportation_method': product_data.get('transportation_method', ''),
            'manufacturing_process': product_data.get('manufacturing_process', ''),
            'certifications': product_data.get('certifications', ''),
            'environmental_benefits': product_data.get('environmental_benefits', ''),
            'usage_advantages': product_data.get('usage_advantages', ''),
            'conventional_impact': product_data.get('conventional_impact', ''),
            'carbon_footprint': product_data.get('carbon_footprint', ''),
            'water_usage': product_data.get('water_usage', ''),
            'recyclability': product_data.get('recyclability', '')
        }
    )
    if created:
        print(f"✓ Product created: {product_data['name']}")
    else:
        # Update existing products with sustainability information
        product.raw_material_source = product_data.get('raw_material_source', '')
        product.transportation_method = product_data.get('transportation_method', '')
        product.manufacturing_process = product_data.get('manufacturing_process', '')
        product.certifications = product_data.get('certifications', '')
        product.environmental_benefits = product_data.get('environmental_benefits', '')
        product.usage_advantages = product_data.get('usage_advantages', '')
        product.conventional_impact = product_data.get('conventional_impact', '')
        product.carbon_footprint = product_data.get('carbon_footprint', '')
        product.water_usage = product_data.get('water_usage', '')
        product.recyclability = product_data.get('recyclability', '')
        product.save()
        print(f"✓ Product updated with sustainability info: {product_data['name']}")

print("\n" + "="*60)
print("SETUP COMPLETE!")
print("="*60)
print("\nYou can now login with:")
print("  Admin:  username: admin,      password: admin123")
print("  Buyer:  username: buyer1,     password: buyer123")
print("  Seller: username: eco_threads or green_wear, password: seller123")
print("\nRun the server: python manage.py runserver")
print("="*60)
