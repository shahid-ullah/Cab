from django.shortcuts import render
from django.views.generic import ListView

from .models import Snippet

class SnippetListView(ListView):
    model = Snippet
    template_name = 'cab/snippet_list.html'

