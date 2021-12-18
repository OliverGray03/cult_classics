from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from products.models import Product
from profiles.models import UserProfile
from favorites.models import Favourite

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

    products = Product.objects.filter(user_favorites=request.user)
    context = {
        'products': products
    }
    return render(request, 'favorites/favorites.html', context)


"""def add_favourite(request, item_id):
    """
    A view to return the about us page
    """
    if not request.user.is_authenticated:
        messages.error(
            request,
            'Sorry! Only members can access favorites'
        )
        return redirect(reverse('home'))

    profile = UserProfile.objects.get(user=request.user)
    product = Product.objects.get(pk=item_id)

    if (profile is null or product is null)
        messages.error(
            request,
            'Sorry! Product or profile doesnt exist'
        )
        return redirect(reverse('home'))
        
    Favourite.objects.create(product = product,
                             user_profile = profile)

    context = {
        'products': products
    }
    return render(request, 'favorites/favorites.html', context)""