from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Post(models.Model):
	poster = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	text = models.TextField()
	source = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	published_date = models.DateTimeField(blank=True, null=True)
	tag1 = models.CharField(max_length=50)
	tag2 = models.CharField(max_length=50)
	tag3 = models.CharField(max_length=50)
	tag4 = models.CharField(max_length=50)
	tag5 = models.CharField(max_length=50)

	class Meta:
		ordering = ['published_date']

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title