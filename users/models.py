from django.db import models
from django.contrib.auth.models import User 
from PIL import Image 
from django.core.files.storage import default_storage as storage

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, **kwargs):
		super().save()

		#img = Image.open(self.image.path)
		img = Image.open(self.image.name))

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.name)

			