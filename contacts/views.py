from django.shortcuts import render, redirect
from .models import Contacts
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage


def contacts(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['listing_id']
        Realtor_email = request.POST['Realtor_email']
        contact = Contacts(listing_id=listing_id, listing=listing, email=email,
                           name=name, phone=phone, message=message, user_id=user_id)

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry for this listing ')
                return redirect('/listings/' + listing_id)

        contact.save()

        # Send email
        send_mail(
            'Property Listing Inquiry',
            'You have an inquiry for' + listing + '. Sign in for more information',
            'armin.arm90@gmail.com',
            [Realtor_email, 'arm.armin90@gmail.com'],
            fail_silently=False

        )
        messages.success(request, ' Your request has submited')
        return redirect('/listings/' + listing_id)

        # def send_email(request):
        #     msg = EmailMessage('Request Callback',
        #                'Here is the message. an inquiry for '+ listing, to=[Realtor_email,'ar.armin90@gmail.com'])
        #     msg.send()
        #     messages.success(request, ' Your request has submited')
        #     return redirect('/listings/' + listing_id)

        # send_email(request)
