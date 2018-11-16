from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse

#each class is its own table in the db
#each attribute will be its own field in db 
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	#if user is deleted, delete Posts 
	author = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.title 


	# tell Django how to find url to any specific instance of a post  
	def get_absolute_url(self):
		# 'post-detail' requires a pk which this kwargs handles
		return reverse('post-detail', kwargs={'pk': self.pk})

