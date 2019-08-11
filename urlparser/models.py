from django.db import models

# Create your models here.
class UrlModel(models.Model):

	url  = models.CharField(max_length=1000, unique=True)
	small_url = models.CharField(max_length=8, primary_key=True)

	class Meta:
		ordering = ['small_url']


