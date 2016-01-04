from django.conf.urls import patterns, include, url

from django.contrib import admin
from sun import views 
# from books.views import search_form
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myfirstproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^hello/$', views.hello),
    (r'^$', views.current_datetime),
    (r'^time/$', views.current_datetime),
    (r'^another/$', views.current_datetime),
    (r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    (r'^browser/$', views.ua_display_good1),
    (r'^search/', include('books.urls')),
    (r'^submit/$', views.submit),
    (r'^contact/$', views.contact),
)
