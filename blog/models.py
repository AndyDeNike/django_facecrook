from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

#each class is its own table in the db
#each attribute will be its own field in db 
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	#if user is deleted, delete Posts 
	author = models.ForeignKey(User, on_delete=models.CASCADE)


