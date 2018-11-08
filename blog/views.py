from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
	#render returns HttpResponse
	return render(request, 'blog/home.html')

def about(request):
	return render(request, 'blog/about.html')