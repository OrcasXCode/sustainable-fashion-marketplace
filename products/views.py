from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product
from .forms import ProductForm
from users.models import SellerProfile


def home(request):
    """Homepage with featured products"""
    products = Product.objects.filter(approved=True)[:8]
    context = {
        'products': products,
        'featured_products': products[:4]
    }
    return render(request, 'products/home.html', context)


def product_list(request):
    """View all approved products with search and filter"""
    products = Product.objects.filter(approved=True)
    
    # Search
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(material__icontains=search_query) |
            Q(seller__brand_name__icontains=search_query)
        )
    
    # Filter by material
    material = request.GET.get('material', '')
    if material:
        products = products.filter(material__icontains=material)
    
    # Sort by price
    sort = request.GET.get('sort', '')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created_at')
    
    context = {
        'products': products,
        'search_query': search_query,
        'material': material,
        'sort': sort,
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    """View product details"""
    product = get_object_or_404(Product, pk=pk, approved=True)
    related_products = Product.objects.filter(
        approved=True,
        seller=product.seller
    ).exclude(pk=pk)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def seller_products(request):
    """Seller's product list"""
    if request.user.role != 'seller':
        messages.error(request, 'Access denied. Sellers only.')
        return redirect('home')
    
    try:
        seller_profile = request.user.seller_profile
    except SellerProfile.DoesNotExist:
        messages.error(request, 'Seller profile not found.')
        return redirect('home')
    
    products = Product.objects.filter(seller=seller_profile)
    context = {'products': products}
    return render(request, 'products/seller_products.html', context)


@login_required
def add_product(request):
    """Add new product"""
    if request.user.role != 'seller':
        messages.error(request, 'Access denied. Sellers only.')
        return redirect('home')
    
    try:
        seller_profile = request.user.seller_profile
    except SellerProfile.DoesNotExist:
        messages.error(request, 'Seller profile not found.')
        return redirect('home')
    
    if not seller_profile.verified:
        messages.warning(request, 'Your seller account is pending verification. You cannot add products yet.')
        return redirect('seller_dashboard')
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = seller_profile
            product.save()
            messages.success(request, 'Product added successfully! Waiting for admin approval.')
            return redirect('seller_products')
    else:
        form = ProductForm()
    
    return render(request, 'products/add_product.html', {'form': form})


@login_required
def edit_product(request, pk):
    """Edit existing product"""
    if request.user.role != 'seller':
        messages.error(request, 'Access denied. Sellers only.')
        return redirect('home')
    
    try:
        seller_profile = request.user.seller_profile
    except SellerProfile.DoesNotExist:
        messages.error(request, 'Seller profile not found.')
        return redirect('home')
    
    product = get_object_or_404(Product, pk=pk, seller=seller_profile)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('seller_products')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/edit_product.html', {'form': form, 'product': product})


@login_required
def delete_product(request, pk):
    """Delete product"""
    if request.user.role != 'seller':
        messages.error(request, 'Access denied. Sellers only.')
        return redirect('home')
    
    try:
        seller_profile = request.user.seller_profile
    except SellerProfile.DoesNotExist:
        messages.error(request, 'Seller profile not found.')
        return redirect('home')
    
    product = get_object_or_404(Product, pk=pk, seller=seller_profile)
    
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('seller_products')
    
    return render(request, 'products/delete_product.html', {'product': product})
