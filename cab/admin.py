from django.contrib import admin

from .models import (
    Language,
    Snippet,
)

class LanguageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Language, LanguageAdmin)

class SnippetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'tags': ("title",)}

admin.site.register(Snippet, SnippetAdmin)
