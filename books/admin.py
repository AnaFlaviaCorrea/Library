from django.contrib import admin
from .models import Books

class AdminContacts(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'description', 'release_year']
    search_fields = ['title']
    list_filter = ['author']
    list_display_links = ['title']

admin.site.register(Books, AdminContacts)
