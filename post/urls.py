from django.urls import path
from post.views import mainindex, index, NewPost, PostDetails, tags, like, favorite, about_us, report_bug, news_forum, setting, shop, trend, helpme, apps


urlpatterns = [
	path('', mainindex, name='index'),
   	path('following/', index, name='following-index'),
   	path('newpost/', NewPost, name='newpost'),
   	path('<uuid:post_id>', PostDetails, name='postdetails'),
   	path('<uuid:post_id>/like', like, name='postlike'),
   	path('<uuid:post_id>/favorite', favorite, name='postfavorite'),
   	path('tag/<slug:tag_slug>', tags, name='tags'),
	path('about', about_us, name='about'),
	path('report', report_bug, name='report_bug'),
	path('news', news_forum, name='news'),
	path('setting', setting, name='setting'),
	path('apps', apps, name='apps'),
	path('shop', shop, name='shop'),
	path('trend', trend, name='trends'),
	path('help', helpme, name='help'),
]