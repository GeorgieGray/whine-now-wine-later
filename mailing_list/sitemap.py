from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class MailingListSitemap(Sitemap):
    def items(self):
        return ['join_news', 'leave_news', 'hello_news', 'bye_news']
    def location(self, item):
        return reverse(item)