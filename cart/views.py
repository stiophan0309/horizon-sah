from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a specified product to the cart"""

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 1)

    request.session['cart'] = cart
    return redirect(reverse('products'))

def remove_from_cart(request, id):
    """Remove a specified product from the cart"""

    cart = request.session.get('cart', {})
    cart.pop(id, None)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))