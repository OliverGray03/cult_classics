from django.contrib import admin
from .models import Favorite

# Register your models here.


class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        'product'
    )

    ordering = ('user_profile',)


admin.site.register(Favorite)
