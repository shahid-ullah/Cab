# from .models import Snippet
from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User


class LanguageManager(models.Manager):
    def top_languages(self):
        top_languages = self.annotate(score=Count('snippet')).order_by('score')
        return top_languages


class SnippetManager(models.Manager):
    def top_authors(self):
        # print(f"self: {self}")
        top_authors = User.objects.annotate(score=Count('snippet')).order_by('score')
        return top_authors

