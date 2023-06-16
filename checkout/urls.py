from django.urls import path
from .views import Checkout, StripeConfig

urlpatterns = [
    path('config/', StripeConfig.as_view()),
    path('<id>/', Checkout.as_view(), name="checkout")
]
