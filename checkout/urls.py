from django.urls import path
from .views import Checkout, ThankYou
from .apis import StripeConfig, StripeSession

urlpatterns = [
    path('api/config/', StripeConfig.as_view()),
    path('api/session/<id>', StripeSession.as_view()),
    path('thank-you/<id>', ThankYou.as_view(), name="thanks"),
    path('<id>/', Checkout.as_view(), name="checkout")
]
