from django.urls import path
from .views import Checkout, ThankYou
from .apis import StripeConfig, StripeSession
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('api/config/', login_required(StripeConfig.as_view())),
    path('api/session/<id>', login_required(StripeSession.as_view())),
    path('thank-you/<id>', login_required(ThankYou.as_view()), name="thanks"),
    path('<id>/', login_required(Checkout.as_view()), name="checkout")
]
