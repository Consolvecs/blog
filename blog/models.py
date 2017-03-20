from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	"""docstring for Post"""
	title = models.CharField(max_length=200)
	author = models.ForeignKey('auth.User')
	text = models.TextField()
	craeted_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=False)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title