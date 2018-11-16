from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
#from django.http import HttpResponse


def home(request):
	context = {
		'posts': Post.objects.all() 
	} 

	#render returns HttpResponse
	return render(request, 'blog/home.html', context)


class PostListView(ListView):
	model = Post 
	template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html 
	context_object_name = 'posts'  
	ordering = ['-date_posted']  #setting ordering attribute on the field you want ordered (- reverses order)

class PostDetailView(DetailView):
	model = Post 
	

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})