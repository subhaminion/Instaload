# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from bs4 import BeautifulSoup
import requests
# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def download(request):
	if request.method=='POST':
		url   = request.POST.get('iurl')
		raw   = requests.get(url)
		soup  = BeautifulSoup(raw.text, 'html.parser')
		links = soup.find(property="og:image")
		image = links.get('content')
		template = loader.get_template('image.html')
		context = {
			'img': image
		}
		return HttpResponse(template.render(context, request))
		# while image != '':
		# 	html = '<img src="'+image+'" align="center">'
		# 	html += '<>'
		# 	return HttpResponse(html)