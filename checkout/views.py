from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MIAC8ERRwgun0ZrdnW4cXbTlLzyNRRN77lHAXpYwgNwI0ec0D1qe71pbFMAiI2tnPfV6M5HU20Ns56lSqnQ6aPY008oFBCzW3',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
