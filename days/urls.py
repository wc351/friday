from django.conf.urls import patterns, include, url
from .views import Monday

urlpatterns = patterns('',
                       url(r'^mondays$', Monday.as_view(), name='monday'),
)
