"""
Script to add product images from placeholder/free image services
"""
import os
import django
import requests
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sustainable_fashion.settings')
django.setup()

from products.models import Product
from django.core.files import File

# Product image URLs from Unsplash (free high-quality images)
# These are placeholder URLs - in production, you'd use actual product photos
product_images = {
    'Organic Cotton T-Shirt': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=800&q=80',  # White t-shirt
    'Recycled Denim Jeans': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=800&q=80',  # Jeans
    'Hemp Blend Hoodie': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=800&q=80',  # Hoodie
    'Bamboo Fiber Dress': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=800&q=80',  # Dress
    'Recycled Polyester Jacket': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=800&q=80',  # Jacket
    'Organic Linen Shirt': 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=800&q=80',  # Linen shirt
}

def download_image(url, product_name):
    """Download image from URL"""
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to download image for {product_name}: Status {response.status_code}")
            return None
    except Exception as e:
        print(f"Error downloading image for {product_name}: {str(e)}")
        return None

def add_images_to_products():
    """Add images to all products"""
    print("Starting to add product images...\n")
    
    for product_name, image_url in product_images.items():
        try:
            product = Product.objects.get(name=product_name)
            
            if product.image:
                print(f"⏭️  {product_name} already has an image, skipping...")
                continue
            
            print(f"📥 Downloading image for {product_name}...")
            image_content = download_image(image_url, product_name)
            
            if image_content:
                # Save image to product
                import tempfile
                with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as img_temp:
                    img_temp.write(image_content)
                    img_temp.flush()
                    
                    # Generate filename
                    filename = f"{product_name.lower().replace(' ', '_')}.jpg"
                    
                    # Save to product
                    with open(img_temp.name, 'rb') as f:
                        product.image.save(filename, File(f), save=True)
                    
                    print(f"✅ Image added to {product_name}")
                
                # Clean up temp file
                try:
                    os.unlink(img_temp.name)
                except:
                    pass
            else:
                print(f"❌ Could not download image for {product_name}")
                
        except Product.DoesNotExist:
            print(f"❌ Product not found: {product_name}")
        except Exception as e:
            print(f"❌ Error processing {product_name}: {str(e)}")
    
    print("\n" + "="*60)
    print("IMAGE IMPORT COMPLETE!")
    print("="*60)

if __name__ == '__main__':
    # Check if requests is installed
    try:
        import requests
    except ImportError:
        print("ERROR: 'requests' library not installed.")
        print("Please run: pip install requests")
        exit(1)
    
    add_images_to_products()
