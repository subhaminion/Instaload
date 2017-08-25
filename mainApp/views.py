# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from bs4 import BeautifulSoup

# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def download(request):
	if request.method=='POST':
		url=request.form('iurl', '')
		# raw=requests.get(url) #make a request to the URL
		# soup=BeautifulSoup(raw.text,'html.parser') #get the HTML

		# links= soup.find(property="og:image") #find meta with property=og:image
		# image=links.get('content') #get its content
		return HttpResponse('kaam ho raha hai')
	# while image!='':
	# 	return '<img src="'+image+'"'+ 'align="center">' #insert content in img tag

	# return render_template('index.html')