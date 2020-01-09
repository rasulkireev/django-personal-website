from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5

    def items(self):
        return ['home', 'about',
                'now', 'wiltw_now',
                'read-books', 'to-read-books', 'currently-reading-books',
                'all_posts']

    def location(self, item):
        return reverse(item)