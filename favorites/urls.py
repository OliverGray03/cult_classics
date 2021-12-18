from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorites, name='favorites'),
    path(
        'add_to_favorites/<product_id>',
        views.add_to_favorites,
        name='add_to_favorites'
    ),
]
