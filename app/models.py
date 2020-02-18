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
    link = models.URLField()
    tags = models.ManyToManyField(Tag)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    created_date = models.DateTimeField(default=timezone.now)
    publish = models.BooleanField(default=False)
    total_hit_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class TutorialHitCount(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tutorial.title + '-' + str(self.created_date)

    def save(self, *args, **kwargs):
        if self.tutorial.publish:
            self.tutorial.total_hit_count = self.tutorial.total_hit_count + 1
            self.tutorial.save()
            super(TutorialHitCount, self).save(*args, **kwargs)
        
