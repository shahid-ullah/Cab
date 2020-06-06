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
    add_bookmark,
    delete_bookmark,
    user_bookmarks,
    most_bookmarked,
)

urlpatterns = [
    path('<int:pk>/', SnippetDetailView.as_view(),
         name='snippet_detail'),
    path('languages/', LanguageListView.as_view(), name='language_list'),
    path('bookmark/<snippet_id>/', add_bookmark, name='add_bookmark'),
    path('bookmark_delete/<snippet_id>/', delete_bookmark,
         name='delete_bookmark'),
    path('crispy/', crispy_view, name='crispy_view'),
    path('top_authors/', top_authors, name='top_authors'),
    path('top_languages/', top_languages, name='top_languages'),
    path('add_snippet/', add_snippet, name='add_snippet'),
    path('edit/<int:snippet_id>/', edit_snippet, name='edit_snippet'),
    path('all/', SnippetListView.as_view(), name='snippet_list'),
    path('all/', SnippetListView.as_view(), name='snippet_list'),
    path('bookmarks/', most_bookmarked, name='bookmarks'),
    path('', user_bookmarks, name='user_bookmarks'),
]
