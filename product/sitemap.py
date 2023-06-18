from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class ProductSitemap(Sitemap):
    def items(self):
        return ['root', 'workout_list', 'create_workout', 'edit_workout', 'delete_workout']
    def location(self, item):
        return reverse(item)