# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from django.conf import settings

def search_form(request):
	c = RequestContext(request, {	
	})
	return render_to_response('books/search_form.html', c)

