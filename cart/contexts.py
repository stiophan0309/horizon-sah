from django.shortcuts import get_object_or_404
from works.models import Work


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    work_count = 0
    
    for id, quantity in cart.items():
        work = get_object_or_404(Work, pk=id)
        total += quantity * work.price
        work_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'work': work})
    
    return {'cart_items': cart_items, 'total': total, 'work_count': work_count}
