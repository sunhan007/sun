# -*- coding: utf-8 -*-

from django.conf.urls import *
import views

urlpatterns = patterns('',
    (r'^search_form/$', views.search_form),
    
)