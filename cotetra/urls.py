from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView, TemplateView, DetailView
from cotetra.network.models import Line, Station
from cotetra.survey.models import Survey

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^station/$', ListView.as_view(model=Station), name="stations"),
    url(r'^station/(?P<pk>\d+)/$', DetailView.as_view(model=Station), name="station"),
    url(r'^line/$', ListView.as_view(model=Line)),
    url(r'^survey/$', ListView.as_view(model=Survey)),
    url(r'^$', TemplateView.as_view(template_name='home.html'))
)
