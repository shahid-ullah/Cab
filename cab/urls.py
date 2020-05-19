# cab/urls.py

from django.contrib import admin
from django.urls import path

from .views import SnippetListView, SnippetDetailView, LanguageListView, top_authors

urlpatterns = [
    path('detail/<int:pk>/', SnippetDetailView.as_view(),
         name='snippet_detail'),
    path('languages/', LanguageListView.as_view(), name='language_list'),
    path('top_authors/', top_authors, name='top_authors'),
    path('', SnippetListView.as_view(), name='snippet_list'),
]
