from django.db import models

from products.models import Product
from profiles.models import UserProfile


class Favorite(models.Model):
    """Model to send a contact message"""
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(
        UserProfile, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "user: " + self.user_profile.user.username + ", product: " + self.product.name
