from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import stripe

class StripeConfig(View):
    @csrf_exempt
    def get(self, request):
        public_key = os.getenv('STRIPE_PUBLISHABLE_KEY')
        return JsonResponse({ 'publicKey': public_key }, safe=False)

class StripeCheckout(View):
    @csrf_exempt
    def get(self, request):
        try:
            host = request.get_host()
            stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

            session = stripe.checkout.Session.create(
                success_url=host + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=host + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {} # TODO
                ]
            )
            return JsonResponse({ 'sessionId': checkout_session['id'] })
        except Exception as e:
            return JsonResponse({ 'error': str(e) })