from django.db import models


class Article(models.Model) :
	title = models.CharField(max_length=255)
	summary = models.CharField(max_length=255)
	full_text = models.TextField()
	category = models.CharField(max_length=255)
	pubdate = models.DateTimeField()


class Image(models.Model) :
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images')

	def __str__(self) :
		return self.title
