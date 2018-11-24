from django.db import models
from django.forms import ModelForm
from django.utils import timezone


class Article(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]
