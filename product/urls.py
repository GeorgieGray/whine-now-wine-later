from django.urls import path
from product.views import Buy

urlpatterns = [
    path('', Buy.as_view(), name="root")
]
