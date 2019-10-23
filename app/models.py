from django.db import models
from django.utils import timezone


class Tag(models.Model):
    """tags have a name, creation date and maybe description"""
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Tutorial(models.Model):
    """tutorials have a title, a URL, a set of tags, a category and creation date"""
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
    link = models.URLField(max_length=1000)
    tags = models.ManyToManyField(Tag)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    created_date = models.DateTimeField(default=timezone.now)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title
