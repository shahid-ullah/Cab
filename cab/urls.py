# cab/urls.py
from django.urls import path

from .views import (
    SnippetListView,
    SnippetDetailView,
    LanguageListView,
    top_authors,
    top_languages,
    add_snippet,
    edit_snippet,
    crispy_view,
)

urlpatterns = [
    path('<int:pk>/', SnippetDetailView.as_view(),
         name='snippet_detail'),
    path('languages/', LanguageListView.as_view(), name='language_list'),
    path('crispy/', crispy_view, name='crispy_view'),
    path('top_authors/', top_authors, name='top_authors'),
    path('top_languages/', top_languages, name='top_languages'),
    path('add_snippet/', add_snippet, name='add_snippet'),
    path('edit/<int:snippet_id>/', edit_snippet, name='edit_snippet'),
    path('', SnippetListView.as_view(), name='snippet_list'),
]
