from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import os
import stripe
from product.models import Product

@method_decorator(csrf_exempt, name='dispatch')
class StripeConfig(View):
    def get(self, request):
        public_key = os.getenv('STRIPE_PUBLISHABLE_KEY')
        return JsonResponse({ 'publicKey': public_key }, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class StripeSession(View):
    def post(self, request, id):
        product = get_object_or_404(Product, pk=id)

        try:
            home = os.getenv("HOME_URL")
            stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

            session = stripe.checkout.Session.create(
                success_url=home + 'checkout/thank-you/' + str(product.id),
                cancel_url=home + 'checkout/' + str(product.id),
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price': product.stripe_price,
                        'quantity': 1
                    }
                ]
            )
            return JsonResponse({ 'sessionId': session['id'] })
        except Exception as e:
            return JsonResponse({ 'error': str(e) })