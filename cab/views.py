from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.db.models import Count
from django.template import loader

from .models import Snippet, Language

class SnippetListView(ListView):
    model = Snippet
    template_name = 'cab/snippet_list.html'


class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'cab/snippet_detail.html'


class LanguageListView(ListView):
    model = Language
    template_name = 'cab/language_list.html'

def top_authors(request):
    top_authors = User.objects.annotate(score=Count('snippet')).order_by('score')
    return render(request, 'cab/top_authors.html', {'authors': top_authors})
