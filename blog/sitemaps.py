from django.contrib.sitemaps import Sitemap
from blog.models import Post


class PostSiteMap(Sitemap):
    changefreq  = 'weekly'
    priority = 0.8

    def items(self):
        return Post.objects.filter(status= 1)

    def lastmod(self, obj):
        return obj.updated_on