from django.db import models
from django.utils import timezone

class tag(models.Model):
	name = models.CharField(max_length=100)
	created_date = models.DateTimeField(default=timezone.now)
	description = models.TextField(blank=True)
	
	def __str__(self):
		return self.name

class tutorial(models.Model):
	ARTICLE = 'article'
	BOOK = 'book'
	CHEATSHEET = 'cheatsheet'
	COURSE = 'course'
	DOCS = 'docs'
	VIDEO = 'video'

	CATEGORIES = (
		(ARTICLE, 'Article'),
		(BOOK, 'Book'),
		(CHEATSHEET, 'Cheatsheet'),
		(COURSE, 'Course'),
		(DOCS, 'Documentation'),
		(VIDEO, 'Video'),
	)

	title = models.CharField(max_length=200)
	link = models.URLField()
	tags = models.ManyToManyField(tag)
	category = models.CharField(max_length=20, choices=CATEGORIES)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title