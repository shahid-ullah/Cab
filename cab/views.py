from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.db.models import Count
from django.template import loader
from django.http import HttpResponseRedirect

from .models import Snippet, Language
from .forms import AddSnippetForm

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
    top_authors = Snippet.objects.top_authors()
    return render(request, 'cab/top_authors.html', {'authors': top_authors})


def top_languages(request):
    top_languages =  Language.objects.top_languages()
    return render(request, 'cab/top_languages.html', {'languages': top_languages})


def add_snippet(request):
    if request.method == "POST":
        form = AddSnippetForm(author=request.user, data=request.POST)
        if form.is_valid():
            new_snippet = form.save()
            return HttpResponseRedirect(new_snippet.get_absolute_url())
    else:
        form = AddSnippetForm(author=request.user)
    return render(request, 'cab/add_snippet.html', {'form': form})
