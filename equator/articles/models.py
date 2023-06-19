from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    preview = models.TextField()
    text = models.TextField()
    img = models.URLField()
    rating = models.IntegerField(default=0)
    cat = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}: {self.title}'
