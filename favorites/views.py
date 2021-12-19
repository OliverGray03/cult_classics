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

    context = {
        'products': [n.product for n in favorites]
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


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    if (request.user.is_authenticated):
        profile = UserProfile.objects.get(user=request.user)
        favorites = Favorite.objects.filter(user_profile=profile)

        for product in products:
            product.isfavorite = favorites.filter(product=product).exists()

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting
    }

    return render(request, 'products/products.html', context)
