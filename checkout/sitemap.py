from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class CheckoutSitemap(Sitemap):
    def items(self):
        return ['checkout', 'thanks']
    def location(self, item):
        return reverse(item)