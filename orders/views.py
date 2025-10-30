from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import CartItem, Order
from products.models import Product


@login_required
def cart_view(request):
    """View cart"""
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.subtotal for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'orders/cart.html', context)


@login_required
def add_to_cart(request, pk):
    """Add product to cart"""
    product = get_object_or_404(Product, pk=pk, approved=True)
    
    if product.stock < 1:
        messages.error(request, 'Product is out of stock.')
        return redirect('product_detail', pk=pk)
    
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )
    
    if not created:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f'{product.name} quantity updated in cart.')
        else:
            messages.warning(request, 'Cannot add more. Stock limit reached.')
    else:
        messages.success(request, f'{product.name} added to cart!')
    
    return redirect('cart')


@login_required
def update_cart(request, pk):
    """Update cart item quantity"""
    cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > 0 and quantity <= cart_item.product.stock:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated.')
        elif quantity > cart_item.product.stock:
            messages.error(request, 'Requested quantity exceeds available stock.')
        else:
            messages.error(request, 'Invalid quantity.')
    
    return redirect('cart')


@login_required
def remove_from_cart(request, pk):
    """Remove item from cart"""
    cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('cart')


@login_required
def checkout(request):
    """Checkout and place order"""
    cart_items = CartItem.objects.filter(user=request.user)
    
    if not cart_items:
        messages.warning(request, 'Your cart is empty.')
        return redirect('cart')
    
    if request.method == 'POST':
        shipping_address = request.POST.get('shipping_address', '')
        
        if not shipping_address:
            messages.error(request, 'Please provide a shipping address.')
            return redirect('checkout')
        
        # Create orders for each cart item
        for item in cart_items:
            if item.product.stock >= item.quantity:
                Order.objects.create(
                    user=request.user,
                    product=item.product,
                    quantity=item.quantity,
                    total_price=item.subtotal,
                    shipping_address=shipping_address
                )
                
                # Update stock
                item.product.stock -= item.quantity
                item.product.save()
            else:
                messages.warning(request, f'Insufficient stock for {item.product.name}. Order not placed.')
        
        # Clear cart
        cart_items.delete()
        messages.success(request, 'Orders placed successfully!')
        return redirect('order_list')
    
    total = sum(item.subtotal for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'orders/checkout.html', context)


@login_required
def order_list(request):
    """View user's orders"""
    orders = Order.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'orders/order_list.html', context)


@login_required
def order_detail(request, pk):
    """View order details"""
    order = get_object_or_404(Order, pk=pk, user=request.user)
    context = {'order': order}
    return render(request, 'orders/order_detail.html', context)


@login_required
def cancel_order(request, pk):
    """Cancel an order"""
    order = get_object_or_404(Order, pk=pk, user=request.user)
    
    if order.status in ['pending', 'confirmed']:
        order.status = 'cancelled'
        order.save()
        
        # Restore stock
        order.product.stock += order.quantity
        order.product.save()
        
        messages.success(request, 'Order cancelled successfully.')
    else:
        messages.error(request, 'This order cannot be cancelled.')
    
    return redirect('order_list')


@login_required
def seller_orders(request):
    """View seller's orders"""
    if request.user.role != 'seller':
        messages.error(request, 'Access denied. Sellers only.')
        return redirect('home')
    
    try:
        seller_profile = request.user.seller_profile
    except:
        messages.error(request, 'Seller profile not found.')
        return redirect('home')
    
    orders = Order.objects.filter(product__seller=seller_profile)
    context = {'orders': orders}
    return render(request, 'orders/seller_orders.html', context)
