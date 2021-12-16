from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    """
    A view to display the contact us page and contact form
    """

    return render(request, 'contact/contact.html')