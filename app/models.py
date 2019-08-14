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

	TUTORIAL_CATEGORIES = (
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
	category = models.CharField(max_length=20, choices=TUTORIAL_CATEGORIES, default=ARTICLE)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title