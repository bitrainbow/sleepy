from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import BlogIndex, BlogDetail
from stories.views import ShortStoryListView, ShortStoryDetailView, PoemListView, PoemDetailView

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^blog/(?P<slug>[\w-]+)', BlogDetail.as_view(), name="entry_detail"),
    url(r'^blog/', BlogIndex.as_view(), name="entry_index"),

    url(r'^poem/(?P<slug>[\w-]+)', PoemDetailView.as_view(), name="poem_detail"),
    url(r'^poem/', PoemListView.as_view(), name="poem_index"),

    url(r'^shortstory/(?P<slug>[\w-]+)', ShortStoryDetailView.as_view(), name="shortstory_detail"),
    url(r'^shortstory/', ShortStoryListView.as_view(), name="shortstory_index"),
)
