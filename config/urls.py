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
from django.views.generic import TemplateView

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
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"))
]

handler404 = 'config.views.custom_page_not_found_view'
handler500 = 'config.views.custom_error_view'
handler403 = 'config.views.custom_permission_denied_view'
handler400 = 'config.views.custom_bad_request_view'