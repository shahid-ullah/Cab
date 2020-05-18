# cab/urls.py

from django.contrib import admin
from django.urls import path

from .views import SnippetListView, SnippetDetailView, LanguageListView

urlpatterns = [
    path('detail/<int:pk>/', SnippetDetailView.as_view(),
         name='snippet_detail'),
    path('languages/', LanguageListView.as_view(), name='language_list'),
    path('', SnippetListView.as_view(), name='snippet_list'),
]
