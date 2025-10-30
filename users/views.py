from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Sum, Q
from .forms import UserRegistrationForm, SellerRegistrationForm, ProfileUpdateForm
from .models import User, SellerProfile
from products.models import Product
from orders.models import Order


def register(request):
    """Buyer registration"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def seller_register(request):
    """Seller registration"""
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Seller registration submitted! Please wait for admin approval.')
            return redirect('seller_dashboard')
    else:
        form = SellerRegistrationForm()
    return render(request, 'users/seller_register.html', {'form': form})


def user_login(request):
    """User login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            
            # Redirect based on role
            if user.role == 'seller':
                return redirect('seller_dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')


def user_logout(request):
    """User logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required
def profile(request):
    """User profile view and edit"""
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    context = {
        'form': form,
        'orders': Order.objects.filter(user=request.user)[:5]
    }
    return render(request, 'users/profile.html', context)


@login_required
def seller_dashboard(request):
    """Seller dashboard"""
    if request.user.role != 'seller':
        messages.error(request, 'Access denied. Sellers only.')
        return redirect('home')
    
    try:
        seller_profile = request.user.seller_profile
    except SellerProfile.DoesNotExist:
        messages.error(request, 'Seller profile not found.')
        return redirect('home')
    
    products = Product.objects.filter(seller=seller_profile)
    orders = Order.objects.filter(product__seller=seller_profile)
    
    stats = {
        'total_products': products.count(),
        'approved_products': products.filter(approved=True).count(),
        'pending_products': products.filter(approved=False).count(),
        'total_orders': orders.count(),
        'total_revenue': orders.filter(status='delivered').aggregate(Sum('total_price'))['total_price__sum'] or 0,
    }
    
    context = {
        'seller_profile': seller_profile,
        'stats': stats,
        'recent_products': products[:5],
        'recent_orders': orders[:10],
    }
    return render(request, 'users/seller_dashboard.html', context)


@login_required
def admin_dashboard(request):
    """Admin dashboard - overview of marketplace"""
    if not request.user.is_staff:
        messages.error(request, 'Access denied. Admin only.')
        return redirect('home')
    
    stats = {
        'total_users': User.objects.count(),
        'total_buyers': User.objects.filter(role='buyer').count(),
        'total_sellers': User.objects.filter(role='seller').count(),
        'verified_sellers': SellerProfile.objects.filter(verified=True).count(),
        'pending_sellers': SellerProfile.objects.filter(verified=False).count(),
        'total_products': Product.objects.count(),
        'approved_products': Product.objects.filter(approved=True).count(),
        'pending_products': Product.objects.filter(approved=False).count(),
        'total_orders': Order.objects.count(),
        'pending_orders': Order.objects.filter(status='pending').count(),
        'delivered_orders': Order.objects.filter(status='delivered').count(),
        'cancelled_orders': Order.objects.filter(status='cancelled').count(),
        'returned_orders': Order.objects.filter(status='returned').count(),
        'total_revenue': Order.objects.filter(status='delivered').aggregate(Sum('total_price'))['total_price__sum'] or 0,
    }
    
    recent_orders = Order.objects.all()[:10]
    pending_products = Product.objects.filter(approved=False)[:10]
    pending_sellers = SellerProfile.objects.filter(verified=False)[:10]
    
    context = {
        'stats': stats,
        'recent_orders': recent_orders,
        'pending_products': pending_products,
        'pending_sellers': pending_sellers,
    }
    return render(request, 'users/admin_dashboard.html', context)
