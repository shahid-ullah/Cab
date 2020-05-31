#  Cab/cab/models.py
import datetime

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from markdown import markdown
from pygments import formatters, highlight, lexers
from tagging.fields import TagField

from .managers import SnippetManager, LanguageManager


class Language(models.Model):
    objects = LanguageManager()
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    language_code = models.CharField(max_length=50)
    mime_type = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    def get_lexer(self):
        return lexers.get_lexer_by_name(self.language_code)


class Snippet(models.Model):
    objects = SnippetManager()
    title = models.CharField(max_length=225)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    code = models.TextField()
    highlighted_code = models.TextField(editable=False)
    tags = TagField()
    pub_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.pub_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        self.description_html = markdown(self.description)
        self.highlighted_code = self.highlight()
        super(Snippet, self).save(force_insert, force_update, using)

    def get_absolute_url(self):
        return reverse("snippet_detail", args=[self.id, ])

    def highlight(self):
        return highlight(self.code, self.language.get_lexer(),
                         formatters.HtmlFormatter(lineos=True))


class Bookmark(models.Model):
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='cab_bookmarks')
    date = models.DateTimeField(editable=False)

    class Meta:
        ordering = ['-date', ]

    def __str__(self):
        return "%s bookmarked by %s" % (self.snippet, self.user)

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.date = datetime.datetime.now()
        super(Bookmark, self).save()
