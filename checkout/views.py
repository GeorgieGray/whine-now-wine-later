from django.views.generic import TemplateView
from product.models import Product
from django.shortcuts import get_object_or_404

class Checkout(TemplateView):
    template_name = "checkout.html"

    def dispatch(self, request, *args, **kwargs):
        id = kwargs.get('id', None)

        self.product = get_object_or_404(Product, pk=id)

        return super(Checkout, self).dispatch(request, *args, **kwargs)