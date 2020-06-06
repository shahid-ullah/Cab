# Cab/cab/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from .forms import SnippetForm, AddressForm
from .models import Snippet, Language, Bookmark


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
    top_languages = Language.objects.top_languages()
    return render(request, 'cab/top_languages.html',
                  {'languages': top_languages})


# def add_snippet(request):
#     if request.method == "POST":
#         form = AddSnippetForm(author=request.user, data=request.POST)
#         if form.is_valid():
#             new_snippet = form.save()
#             return HttpResponseRedirect(new_snippet.get_absolute_url())
#     else:
#         form = AddSnippetForm(author=request.user)
#     return render(request, 'cab/add_snippet.html', {'form': form})

def add_snippet(request):
    if request.method == "POST":
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            new_snippet = form.save(commit=False)
            new_snippet.author = request.user
            new_snippet.save()
            return HttpResponseRedirect(new_snippet.get_absolute_url())
    else:
        form = SnippetForm()
        return render(request, 'cab/add_snippet.html', {'form': form, 'add':
                                                        True})


def edit_snippet(request, snippet_id):
    # print(f"snippet id: {snippet_id}")
    snippet = get_object_or_404(Snippet, id=snippet_id)
    # print(f"snippet id: {snippet_id}")
    if request.user.id != snippet.author.id:
        return HttpResponseForbidden()
    if request.method == "POST":
        form = SnippetForm(instance=snippet, data=request.POST)
        if form.is_valid():
            snippet = form.save()
            return HttpResponseRedirect(snippet.get_absolute_url())
    else:
        form = SnippetForm(instance=snippet)
        return render(request, 'cab/add_snippet.html', {"form": form, 'add':
                                                        False})


def crispy_view(request):
    form = AddressForm
    return render(request, 'cab/crispy_template.html', {"form": form, })


@login_required
def add_bookmark(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    try:
        Bookmark.objects.get(user__pk=request.user.id,
                             snippet__pk=snippet_id)
    except Bookmark.DoesNotExist:
        Bookmark.objects.create(
                            user=request.user,
                            snippet=snippet)
    return HttpResponseRedirect(snippet.get_absolute_url())


def delete_bookmark(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)

    if request.method == "POST":
        Bookmark.objects.filter(user__pk=request.user.id,
                                snippet__pk=snippet.id).delete()
        return HttpResponseRedirect(snippet.get_absolute_url())
    else:
        return render(request, "cab/confirm_bookmark_delete.html",
                      {"snippet": snippet})


def user_bookmarks(request):
    queryset = Bookmark.objects.filter(user__pk=request.user.id)
    return render(request, "cab/user_bookmarks.html", {"bookmarks": queryset})


def most_bookmarked(request):
    bookmarks = Snippet.objects.most_bookmarked()
    return render(request, "cab/most_bookmarked.html",
                  {"bookmarks": bookmarks, })
