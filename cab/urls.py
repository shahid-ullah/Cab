# cab/urls.py

from django.contrib import admin
from django.urls import path

from .views import SnippetListView

urlpatterns = [
    path('', SnippetListView.as_view(), name='snippet_list'),
]
