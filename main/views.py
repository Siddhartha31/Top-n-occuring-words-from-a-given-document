from django.shortcuts import render
from .models import Ans
from bs4 import BeautifulSoup
import requests
from django.template.response import TemplateResponse
import itertools
from django.http import HttpResponse

def homepage(request):
	return render(request=request,
					template_name='sub/home.html',context={"Answer":'answer'})
def freq(request):
	n= int(request.POST['n'],10)
	r=requests.get("https://terriblytinytales.com/test.txt")
	string=r.text
	string=string.split()
	str1={}
	str2=[]
	out={}
	u=0
	for i in string:
		if i not in str2:
			str2.append(i)
	for i in range(0,len(str2)):
		str1[str2[i]]=string.count(str2[i])
	str1=dict(sorted(str1.items(),key=lambda x:x[1],reverse=True))
	if n<len(str1):
		for i,j in str1.items():
			if u!=n:
				out[i]=j
				u=u+1
			else:
				break
		return TemplateResponse(request, 'sub/home.html', {'Answer':out })
	else:
		return HttpResponse('<h1> Incorrect Value </h1>')	
	
	
	





