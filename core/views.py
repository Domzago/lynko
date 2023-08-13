from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def pricing(request):
    return render(request, 'core/pricing.html')


@login_required
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['key']= settings.STRIPE_PUBLISHABLE_KEY
    return context

@login_required
def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount = 100,
            currency = 'usd',
            description = 'link payment',
            source = request.POST['stripeToken']

        )
        return render(request, 'core/charge.html',{
            'charge':charge
        })
