from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property

TUTORIAL_CATEGORIES = (
    ('article', 'article'),
    ('video', 'video'),
    ('course', 'course'),
    ('docs', 'docs'),
)


class tag(models.Model):
	name = models.CharField(max_length=100)
	created_date = models.DateTimeField(default=timezone.now)
	description = models.TextField(blank=True)
	
	def __str__(self):
		return self.name


class tutorial(models.Model):
	title = models.CharField(max_length=200)
	link = models.URLField()
	tags = models.ManyToManyField(tag)
	category = models.CharField(max_length=200, choices = TUTORIAL_CATEGORIES)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
		