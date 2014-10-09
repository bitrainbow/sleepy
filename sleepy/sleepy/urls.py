from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import BlogIndex, BlogDetail

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^blog/(?P<slug>\S)+', BlogDetail.as_view(), name="entry_detail"),
    url(r'^blog/', BlogIndex.as_view(), name="entry_index")
)
