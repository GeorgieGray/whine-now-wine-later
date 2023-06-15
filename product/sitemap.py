from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class ProductSitemap(Sitemap):
    def items(self):
        return ['root']
    def location(self, item):
        return reverse(item)