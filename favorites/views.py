from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models.functions import Lower
from products.models import Product
from profiles.models import UserProfile
from favorites.models import Favorite

from products.models import Product, Category
from products.forms import ProductForm

# Create your views here.


def favorites(request):
    """
    A view to return products which have been added
    to the user's favorites
    """

    if not request.user.is_authenticated:
        messages.error(
            request,
            'Sorry! Only members can access favorites'
        )
        return redirect(reverse('home'))

    profile = get_object_or_404(UserProfile, user=request.user)
    favorites = Favorite.objects.filter(user_profile=profile)

    products = []
    for favorite in favorites:
        product = favorite.product
        product.isfavorite = True
        products.append(product)

    context = {
        'products': products
    }
    return render(request, 'favorites/favorites.html', context)


def add_to_favorites(request, product_id):

    # A view to add a product to favorites

    if not request.user.is_authenticated:
        messages.error(
            request,
            'Sorry! Only members can access favorites'
        )
        return redirect(reverse('home'))

    profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    Favorite.objects.create(product=product,
                            user_profile=profile)

    messages.success(request,
                     (f'Added {product.name} to your favorites'))

    return redirect(reverse('products'))


def remove_from_favorites(request, product_id):

    # A view to remove a product from favorites

    if not request.user.is_authenticated:
        messages.error(
            request,
            'Sorry! Only members can access favorites'
        )
        return redirect(reverse('home'))

    profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    Favorite.objects.get(product=product, user_profile=profile).delete()

    messages.success(request,
                     (f'Removed {product.name} from your favorites'))

    return redirect(reverse('products'))
