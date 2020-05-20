# cab/urls.py

from django.contrib import admin
from django.urls import path

from .views import (
    SnippetListView, SnippetDetailView, LanguageListView, top_authors,
    top_languages,
    add_snippet,
)

urlpatterns = [
    path('<int:pk>/', SnippetDetailView.as_view(),
         name='snippet_detail'),
    path('languages/', LanguageListView.as_view(), name='language_list'),
    path('top_authors/', top_authors, name='top_authors'),
    path('top_languages/', top_languages, name='top_languages'),
    path('add_snippet/', add_snippet, name='add_snippet'),
    path('', SnippetListView.as_view(), name='snippet_list'),
]
