from django.db import models
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from works.models import Work
from accounts.models import Profile
from accounts.forms import ProfileForm
import stripe


# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    user_id = request.user.pk
    # retrieves the Profile info of the current user
    if Profile.objects.filter(user=user_id).exists():
        # turns Profile info to a single variable
        currentprofile = Profile.objects.get(user=user_id)
        form = ProfileForm(initial={'full_name': currentprofile.full_name,
                                    'phone_number':
                                    currentprofile.phone_number,
                                    'country': currentprofile.country,
                                    'postcode': currentprofile.postcode,
                                    'town_or_city':
                                    currentprofile.town_or_city,
                                    'street_address1':
                                    currentprofile.street_address1,
                                    'street_address2':
                                    currentprofile.street_address2,
                                    'county': currentprofile.county,
                                    'user': user_id})
    else:
        form = OrderForm
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                work = get_object_or_404(Work, pk=id)
                total += quantity * work.price
                order_line_item = OrderLineItem(
                    order=order,
                    work=work,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer is not None:
                if customer.paid:
                    messages.error(request, "You have successfully paid")
                    request.session['cart'] = {}
                    return redirect(reverse('works'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
