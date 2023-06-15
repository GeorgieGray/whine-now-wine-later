from django.views.generic import ListView
from .models import Product

class Buy(ListView):
    template_name = "buy.html"
    model = Product