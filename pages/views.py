from django.shortcuts import render
from listings.choices import price_choices,state_choices,bedroom_choices
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor



def index(request):
    Listings = Listing.objects.order_by('-list_Date').filter(is_publishred=True)[:3]

    context ={
        'listings' : Listings,
        'state_choices' :state_choices,
        'price_choices' : price_choices,
        'bedroom_choices' :bedroom_choices
    }
    
    return render(request, 'pages/index.html',context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    
    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    
    context = {
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors
    }
    return render(request, 'pages/about.html',context)
