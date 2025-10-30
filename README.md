# Sustainable Fashion Marketplace

A Django-based MVP marketplace connecting eco-friendly fashion brands with conscious buyers.

## Features

### User Roles
- **Admin**: Full platform management, seller verification, product approval
- **Seller**: List products, manage inventory, view orders
- **Buyer**: Browse products, shop, place orders

### Core Functionality
- Role-based authentication (Admin, Seller, Buyer)
- Seller verification system
- Product listing and management
- Product approval workflow
- Shopping cart functionality
- Order management system
- Search and filter products
- Dashboard analytics for all user types
- Modern black & white UI/UX

## Quick Start

### Prerequisites
- Python 3.8+
- Django 5.2+

### Installation

1. **Install Dependencies**
   ```bash
   pip install django pillow
   ```

2. **Run Migrations** (Already done)
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Load Sample Data** (Already done)
   ```bash
   python setup_data.py
   ```

4. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**
   - Main Site: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/

## 👤 Test Accounts

### Admin Account
- **Username**: `admin`
- **Password**: `admin123`
- **Access**: Admin Dashboard + Django Admin Panel

### Buyer Account
- **Username**: `buyer1`
- **Password**: `buyer123`
- **Access**: Browse products, shopping cart, orders

### Seller Accounts
- **Username**: `eco_threads` or `green_wear`
- **Password**: `seller123`
- **Access**: Seller dashboard, product management, orders

## 📁 Project Structure

```
django-ca2/
├── sustainable_fashion/    # Main project settings
├── users/                  # User authentication & profiles
├── products/              # Product management
├── orders/                # Cart & order management
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── users/            # User templates
│   ├── products/         # Product templates
│   └── orders/           # Order templates
├── static/               # Static files
│   ├── css/             # Stylesheets
│   └── js/              # JavaScript
├── media/               # User uploads
└── manage.py           # Django management script
```

## 🎨 Design Theme

**Modern Black & White**
- Clean, minimalist interface
- High contrast for accessibility
- Professional and elegant
- Responsive design
- Modern typography (Inter font)

## Key URLs

| URL | Description | Access |
|-----|-------------|--------|
| `/` | Homepage | Public |
| `/products/` | All products | Public |
| `/register/` | Buyer registration | Public |
| `/seller/register/` | Seller registration | Public |
| `/login/` | User login | Public |
| `/cart/` | Shopping cart | Authenticated |
| `/orders/` | User orders | Buyer |
| `/seller/dashboard/` | Seller dashboard | Seller |
| `/admin/dashboard/` | Admin dashboard | Admin |
| `/admin/` | Django admin panel | Admin |

## 🛠️ Admin Features

1. **Dashboard Overview**
   - Total users, sellers, products, orders
   - Revenue tracking
   - Pending approvals

2. **Seller Management**
   - Approve/reject seller registrations
   - Verify brands
   - View seller details

3. **Product Management**
   - Approve/reject product listings
   - Monitor inventory
   - Content moderation

4. **Order Management**
   - View all orders
   - Track order status
   - Monitor returns/cancellations

## 👔 Seller Features

1. **Dashboard**
   - Sales statistics
   - Product performance
   - Order summary

2. **Product Management**
   - Add new products
   - Edit existing products
   - Manage inventory
   - Track approval status

3. **Order Tracking**
   - View orders for their products
   - Monitor order status

## 🛍️ Buyer Features

1. **Product Browsing**
   - Search and filter
   - View product details
   - Sustainable material information

2. **Shopping**
   - Add to cart
   - Update quantities
   - Checkout with COD

3. **Order Management**
   - View order history
   - Track order status
   - Cancel orders

## 📊 Database Models

### User
- Extended Django User model
- Role field (admin/seller/buyer)
- Contact information

### SellerProfile
- Brand information
- Verification status
- Brand description

### Product
- Product details
- Material information
- Stock management
- Approval status

### CartItem
- User cart items
- Quantity tracking

### Order
- Order details
- Status tracking
- Shipping information

## 🔒 Security Features

- CSRF protection
- Password validation
- Role-based access control
- Login required decorators
- Secure admin panel

## MVP Scope

This is an MVP (Minimum Viable Product) with:
- Basic authentication
- Product listing & approval
- Simple checkout (COD)
- Local file storage
- SQLite database

## Future Enhancements

- Payment gateway integration (Stripe/PayPal)
- Email notifications
- Product reviews & ratings
- Advanced search & filters
- Wishlist functionality
- Multi-image upload
- Order tracking with status updates
- Analytics dashboard
- API endpoints for mobile app
- PostgreSQL for production
- AWS S3 for media storage

## Development Notes

- Django Templates for frontend (no separate frontend framework)
- Black & white color scheme throughout
- Modern, clean UI/UX
- Responsive design
- Ready for API/React expansion

## Contributing

This is a learning/demonstration project. Feel free to:
- Report issues
- Suggest features
- Submit pull requests

## 📄 License

This project is for educational purposes.

---

**Built with Django ❤️ for Sustainable Fashion**
