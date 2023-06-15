from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class UserSitemap(Sitemap):
    def items(self):
        return ['login', 'logout', 'register']
    def location(self, item):
        return reverse(item)