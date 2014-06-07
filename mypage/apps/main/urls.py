__author__ = 'abner'

from django.conf.urls import patterns, url

urlpatterns = patterns('mypage.apps.main.views',
                       url(r'^$','index_view', name="url_index"))