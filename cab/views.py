from django.shortcuts import render
from django.views.generic import ListView, DetailView

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
