import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from pygments import formatters, highlight, lexers
from markdown import markdown
from tagging.fields import TagField


class Language(models.Model):
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

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.pub_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        self.description_html = markdown(self.description)
        self.highlighted_code = self.highlight()
        super(Snippet, self).save(force_insert, force_update)

    def get_absolute_url(self):
        return reverse("snippet_detail/", args=[self.id,])

    def highlight(self):
        return highlight(self.code, self.language.get_lexer(),
                         formatters.HtmlFormatter(lineos=True))
