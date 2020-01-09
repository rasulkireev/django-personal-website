"""pw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

# Sitemap imports
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from writings.models import Post
from books.models import Book

sitemaps = {
    'writings': GenericSitemap({
        'queryset': Post.objects.all(),
        'date_field': 'date',
    }, priority=0.9),

    'books': GenericSitemap({
        'queryset': Book.objects.all(),
        'date_field': 'date_published',
    }, priority=0.9),
}

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('rk-admin/', admin.site.urls),
    path('', include('pages.urls')),

    path('now/', include('now.urls')),
    path('what-i-learnt-this-week/', include('wiltw.urls')),
    path('writings/', include('writings.urls')),
    path('health/', include('health.urls')),
    path('books/', include('books.urls')),
    path('api/v1/', include('api.urls')),
    
    path('martor/', include('martor.urls')),
    path('sentry-debug/', trigger_error),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
