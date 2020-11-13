from django.urls import path, include
from django.contrib import admin

from blog.views import (PostList, post_detail, SeriaAPost,
                        PostDetail, EplPost, League1Post,
                        BundesligaPost, LaligaPost,)


app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name = 'home'),
    path('EPL', EplPost.as_view(), name = 'epl'), 
    path('Laliga', LaligaPost.as_view(), name = 'laliga'),
    path('Seria-A', SeriaAPost.as_view(), name = 'seriaA'),
    path('League-1', League1Post.as_view(), name = 'league1'),
    path('Bundesliga', BundesligaPost.as_view(), name = 'bundesliga'),
    path('<slug:slug>', post_detail, name = 'post_detail'),
     path('admini/', admin.site.urls, name = 'admin'),
   
 
]