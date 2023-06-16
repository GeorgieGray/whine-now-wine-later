from django.urls import path
from .views import Checkout
from .apis import StripeConfig, StripeSession

urlpatterns = [
    path('api/config/', StripeConfig.as_view()),
    path('api/session/', StripeSession.as_view()),
    path('<id>/', Checkout.as_view(), name="checkout")
]
