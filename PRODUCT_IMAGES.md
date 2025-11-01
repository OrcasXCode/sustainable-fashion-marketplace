# Product Images - Quick Reference

## ✅ Images Successfully Added!

All 6 products now have high-quality images from Unsplash (royalty-free):

### Product Images List

1. **Organic Cotton T-Shirt** 
   - Image: `organic_cotton_t-shirt.jpg`
   - White/cream t-shirt on neutral background
   - Size: ~55 KB

2. **Recycled Denim Jeans**
   - Image: `recycled_denim_jeans.jpg`
   - Blue denim jeans display
   - Size: ~50 KB

3. **Hemp Blend Hoodie**
   - Image: `hemp_blend_hoodie.jpg`
   - Comfortable hoodie styling
   - Size: ~158 KB

4. **Bamboo Fiber Dress**
   - Image: `bamboo_fiber_dress.jpg`
   - Elegant dress presentation
   - Size: ~176 KB

5. **Recycled Polyester Jacket**
   - Image: `recycled_polyester_jacket.jpg`
   - Modern jacket design
   - Size: ~143 KB

6. **Organic Linen Shirt**
   - Image: `organic_linen_shirt.jpg`
   - Natural linen shirt display
   - Size: ~84 KB

## Location

All images are stored in: `media/products/`

## View Products

Visit the marketplace to see the images in action:
- **Homepage**: http://127.0.0.1:8000/
- **All Products**: http://127.0.0.1:8000/products/
- **Individual Product Pages**: Click any product to see full details with image

## Adding More Images

### For New Products (Sellers)

1. Login as a seller
2. Go to "Add Product"
3. Upload your product image in the "Image" field
4. Supported formats: JPG, PNG, WEBP
5. Recommended size: 800x800px or larger
6. Keep file size under 5MB

### Using the Image Import Script

If you need to add images programmatically:

```bash
python add_product_images.py
```

**Note**: The script will:
- Download images from Unsplash URLs
- Skip products that already have images
- Save images to `media/products/`
- Update the database automatically

### Manual Image Upload

1. Place your image in `media/products/` folder
2. Use Django admin to assign it to a product:
   - Go to http://127.0.0.1:8000/admin/
   - Navigate to Products
   - Edit the product
   - Upload image
   - Save

## Image Display Locations

Images are now visible on:

✅ **Homepage** - Featured products grid
✅ **Product List Page** - All products with images
✅ **Product Detail Page** - Large product image
✅ **Seller Products Page** - Seller's product management
✅ **Cart Page** - Products in shopping cart
✅ **Checkout Page** - Order review
✅ **Order Detail Page** - Purchased items
✅ **Admin Dashboard** - Product listings

## Image Quality Tips

For sellers uploading their own images:

- **Resolution**: 800x800px minimum (square ratio works best)
- **Format**: JPG for photos, PNG for graphics
- **File Size**: Keep under 2MB for faster loading
- **Lighting**: Good natural lighting, clear focus
- **Background**: Clean, neutral backgrounds work best
- **Angles**: Show product from multiple angles if possible
- **Context**: Show product being worn or in use

## Troubleshooting

### Images Not Showing?

1. **Check if file exists**:
   ```bash
   dir media\products
   ```

2. **Verify media URL settings** in `settings.py`:
   - MEDIA_URL = '/media/'
   - MEDIA_ROOT = BASE_DIR / 'media'

3. **Check URLs configuration** - Make sure `urls.py` includes:
   ```python
   from django.conf.urls.static import static
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

4. **Restart the server**:
   ```bash
   python manage.py runserver
   ```

### Re-run Image Import

If you need to re-download images:

1. Delete existing images from `media/products/`
2. Run the script again:
   ```bash
   python add_product_images.py
   ```

## Image Sources

Current images are sourced from:
- **Unsplash** - Free high-quality stock photos
- All images are royalty-free for commercial use
- No attribution required (but appreciated!)

For production, replace with:
- Actual product photography
- Professional styled shots
- Multiple angles per product
- Lifestyle images showing products in use

---

**Server Status**: ✅ Running at http://127.0.0.1:8000/

**All 6 products now have images!** Visit the marketplace to see them live!
