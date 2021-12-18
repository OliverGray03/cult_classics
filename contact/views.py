from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    """
    A view to display the contact us page and contact form
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = request.POST.get('subject')
            name = request.POST.get('name')
            email = request.POST.get('email')
            form.save()
            messages.success(
                request,
                f'Thanks {name}! {subject} has been sent to the \
                    Cult Classics team.'
            )
            # Email confirmation of contact message
            data = form.save()
            subject = render_to_string(
                'contact/confirmation_emails/contact_message_subject.txt',
                {'data': data}
            )
            body = render_to_string(
                'contact/confirmation_emails/contact_message_body.txt',
                {'data': data}
            )
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )
        else:
            messages.error(
                request,
                "Failed to send message, please ensure all fields are correct"
            )

    form = ContactForm()

    context = {
        "form": form
    }
    return render(request, 'contact/contact.html', context)
