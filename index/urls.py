from django.conf.urls import url
from django.contrib import admin
from .views import *


urlpatterns = [
    url(r'^login/$', login_views),
    url(r'^logout/$', logout_views),
    url(r'^register/$', register_views),
    url(r'^$', index_views),
    url(r'^check_uphone/$', check_uphone_views),
    url(r'^goods/$', goods_views),

]
