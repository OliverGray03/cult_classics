from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K3fQXHnlsjvwT2clD9Eu9Rv3XaV8yftmloc3meq0TQN5mZ9k0XUfFTyXTXM5dgxhm7U7Co3VCMjxIZcZPsVpVOJ00lLV5L0FA',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
