from django.shortcuts import render, get_object_or_404
from .models import Offer
# Create your views here.
def index(request):
    offers = Offer.objects.order_by('-pub_date')
    open_offers = offers.filter(offer_status='O')
    closed_offers = offers.filter(offer_status='C')
    context = {
        'open': open_offers,
        'closed': closed_offers,
    }
    return render(request, 'offers/offers.html', context)

def offer(request, offer_id):
    offer = get_object_or_404(Offer, pk = offer_id)
    context = {
        'offer': offer,
    }
    return render(request, 'offers/offer.html', context)
