from django.views.generic import TemplateView, View
from product.models import Product
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

class Checkout(TemplateView):
    template_name = "checkout.html"

    def dispatch(self, request, *args, **kwargs):
        id = kwargs.get('id', None)

        self.product = get_object_or_404(Product, pk=id)

        return super(Checkout, self).dispatch(request, *args, **kwargs)

class StripeConfig(View):

    @csrf_exempt
    def get(self, request):
        public_key = os.getenv('STRIPE_PUBLISHABLE_KEY')
        return JsonResponse({ 'publicKey': public_key }, safe=False)