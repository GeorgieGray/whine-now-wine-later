from django.contrib import admin
from django.urls import path
from product.views import Buy
from user.views import Login, Register, Logout
from django.conf.urls import include
from django.contrib.sitemaps.views import sitemap
from user.sitemap import UserSitemap
from product.sitemap import ProductSitemap
from checkout.sitemap import CheckoutSitemap
from mailing_list.sitemap import MailingListSitemap

sitemaps = {
    'product': ProductSitemap,
    'user': UserSitemap,
    'checkout': CheckoutSitemap,
    'mail': MailingListSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('user/', include('user.urls')),
    path("checkout/", include('checkout.urls')),
    path("mail/", include('mailing_list.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps})
]
