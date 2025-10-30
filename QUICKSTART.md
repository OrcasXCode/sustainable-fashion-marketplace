# Quick Start Guide

## Your Sustainable Fashion Marketplace is Ready! 

The development server is running at: **http://127.0.0.1:8000/**

---

## What You Can Do Now

### 1️⃣ Browse the Marketplace (No Login Required)
- Visit **http://127.0.0.1:8000/** to see the homepage
- Click **Products** to view all sustainable fashion items
- Use search and filters to find specific products

### 2️⃣ Login as Admin
- Go to **http://127.0.0.1:8000/admin/dashboard/** or click "Admin Dashboard" after login
- **Username**: `admin`
- **Password**: `admin123`

**What you can do:**
- View platform statistics (users, products, orders, revenue)
- Approve/reject seller registrations
- Approve/reject product listings
- Manage all platform data via Django admin panel

### 3️⃣ Login as Buyer
- Go to **http://127.0.0.1:8000/login/**
- **Username**: `buyer1`
- **Password**: `buyer123`

**What you can do:**
- Browse and search products
- Add items to cart
- Place orders (Cash on Delivery)
- View order history
- Update profile

### 4️⃣ Login as Seller
- Go to **http://127.0.0.1:8000/login/**
- **Username**: `eco_threads` or `green_wear`
- **Password**: `seller123`

**What you can do:**
- View seller dashboard with statistics
- Add new products (with material info)
- Edit/delete your products
- View orders for your products
- Track sales and revenue

---

## 📱 Key Features to Test

### For Buyers:
1. **Search Products**: Use the search bar on the products page
2. **Add to Cart**: Click "Add to Cart" on product detail pages
3. **Checkout**: 
   - Go to cart
   - Click "Proceed to Checkout"
   - Enter shipping address
   - Place order
4. **Track Orders**: View order status in "My Orders"

### For Sellers:
1. **Add Product**:
   - Go to Seller Dashboard
   - Click "Add Product"
   - Fill in product details (name, price, material, image)
   - Submit for admin approval
2. **Manage Inventory**: Edit product stock and details
3. **View Orders**: Check orders placed for your products

### For Admins:
1. **Approve Sellers**: 
   - Go to Admin Dashboard
   - Review pending seller registrations
   - Click "Review" and approve in Django admin
2. **Approve Products**:
   - View pending products
   - Review and approve/reject listings
3. **Monitor Platform**: View statistics and metrics

---

## UI/UX Highlights

- **Clean Black & White Theme** - Modern, professional design
- **Responsive Design** - Works on all screen sizes
- **Intuitive Navigation** - Easy to find what you need
- **Clear Call-to-Actions** - Prominent buttons and links
- **Status Badges** - Visual indicators for order/product status
- **Dashboard Analytics** - Stats cards for quick overview

---

## Sample Data Included

**2 Verified Sellers**:
- EcoThreads (eco_threads)
- GreenWear (green_wear)

**6 Approved Products**:
- Organic Cotton T-Shirt (₹2499)
- Recycled Denim Jeans (₹6499)
- Hemp Blend Hoodie (₹5499)
- Bamboo Fiber Dress (₹7499)
- Recycled Polyester Jacket (₹10999)
- Organic Linen Shirt (₹4599)

---

## Security Features

- Role-based access control (Admin, Seller, Buyer)
- Login required for sensitive actions
- CSRF protection on all forms
- Password validation
- Secure admin panel

---

## Development Workflow

### Creating a New User Account:
1. Go to **http://127.0.0.1:8000/register/** (for buyers)
2. Or **http://127.0.0.1:8000/seller/register/** (for sellers)

### Seller Verification Process:
1. Seller registers
2. Admin reviews in Django admin panel
3. Admin approves by checking "Verified" checkbox
4. Seller can now list products

### Product Approval Process:
1. Seller adds product
2. Product shows as "Pending" in seller dashboard
3. Admin reviews in Django admin or Admin Dashboard
4. Admin approves by checking "Approved" checkbox
5. Product appears on marketplace

---

## Testing Scenarios

### Scenario 1: Complete Buyer Journey
1. Browse products as guest
2. Register as buyer
3. Add multiple products to cart
4. Update quantities
5. Checkout with shipping address
6. View order status

### Scenario 2: Seller Journey
1. Register as seller
2. Wait for admin approval (or approve yourself via admin)
3. Add product with sustainable material info
4. Wait for product approval
5. View product in marketplace
6. Check order when someone purchases

### Scenario 3: Admin Workflow
1. Login as admin
2. View dashboard statistics
3. Approve pending seller
4. Approve pending product
5. Monitor orders and revenue

---

## URL Cheat Sheet

| What | URL | Who Can Access |
|------|-----|----------------|
| Homepage | http://127.0.0.1:8000/ | Everyone |
| Products | http://127.0.0.1:8000/products/ | Everyone |
| Login | http://127.0.0.1:8000/login/ | Everyone |
| Register (Buyer) | http://127.0.0.1:8000/register/ | Everyone |
| Register (Seller) | http://127.0.0.1:8000/seller/register/ | Everyone |
| Cart | http://127.0.0.1:8000/cart/ | Logged in buyers |
| My Orders | http://127.0.0.1:8000/orders/ | Logged in buyers |
| Profile | http://127.0.0.1:8000/profile/ | All logged in users |
| Seller Dashboard | http://127.0.0.1:8000/seller/dashboard/ | Sellers only |
| My Products | http://127.0.0.1:8000/seller/products/ | Sellers only |
| Add Product | http://127.0.0.1:8000/seller/products/add/ | Verified sellers |
| Admin Dashboard | http://127.0.0.1:8000/admin/dashboard/ | Admins only |
| Django Admin | http://127.0.0.1:8000/admin/ | Admins only |

---

## 💡 Pro Tips

1. **Use Django Admin Panel** for bulk operations and detailed data management
2. **Test with different roles** to see role-based access control in action
3. **Add product images** to make the marketplace more realistic
4. **Check mobile responsiveness** by resizing your browser
5. **Monitor the terminal** to see Django's debug messages

---

## 🐛 Troubleshooting

### Server not running?
```bash
cd c:\Users\Admin\OneDrive\Desktop\django-ca2
python manage.py runserver
```

### Need to reset data?
```bash
# Delete database
del db.sqlite3

# Recreate
python manage.py migrate
python setup_data.py
```

### Forgot admin password?
```bash
python manage.py changepassword admin
```

---

## 📚 Next Steps

1. **Customize the design** - Edit `static/css/style.css`
2. **Add more features** - Product reviews, wishlist, etc.
3. **Integrate payment** - Add Stripe or PayPal
4. **Deploy to production** - Heroku, AWS, or DigitalOcean
5. **Add email notifications** - Django email backend
6. **Create an API** - Django REST Framework for mobile app

---

## What's Included

### 3 Complete User Portals
- Admin Portal with analytics
- Seller Portal with dashboard
- Buyer Portal with shopping features

### Full E-commerce Flow
- Product browsing and search
- Shopping cart
- Checkout process
- Order management

### Admin Features
- User management
- Seller verification
- Product approval
- Order monitoring
- Revenue tracking

### Modern UI/UX
- Black & white theme
- Clean, minimal design
- Responsive layout
- Smooth animations
- Toast notifications

---

**Happy Testing! Your sustainable fashion marketplace is live and ready to use!**

Need help? Check the README.md for detailed documentation.
