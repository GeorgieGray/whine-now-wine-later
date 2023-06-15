from django.urls import path
from .views import Checkout

urlpatterns = [
    path('<id>/', Checkout.as_view(), name="checkout")
]
