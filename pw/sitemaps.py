from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5

    def items(self):
        return ['home',
                'about',
                'now',
                'all_posts']

    def location(self, item):
        return reverse(item)