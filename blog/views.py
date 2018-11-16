from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

# PostCreateView/PostUpdateView share the same template, post_form.html
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post 
	fields = ['title', 'content']

	# Before you submit form, take instance and set it to current user
	def form_valid(self, form):
		# sets author before Post is created 
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post 
	fields = ['title', 'content']

	# Before you submit form, take instance and set it to current user
	def form_valid(self, form):
		# sets author before Post is created 
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		#this gets current user and checks if its equal to the post at hand
		if self.request.user == post.author: 
			return True 
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post 
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author: 
			return True 
		return False


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})