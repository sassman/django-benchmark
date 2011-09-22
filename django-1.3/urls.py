from django.conf.urls.defaults import patterns, include, url

from DjangoBenchmark.views import HelloWorldView

urlpatterns = patterns('',
    (r'^$', HelloWorldView.as_view()),
)
