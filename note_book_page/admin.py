from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest

from .models import NoteBookPage, Category, Tag


class NoteBookPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'category', 'status', 'created_at')
    list_filter = ('tags', 'author', 'status')
    search_fields = ('author', 'category')
    ordering = ('-created_at',)
    
    def get_readonly_fields(self, request, obj=None,):
        if not obj:
            return ('author', 'slug')
        
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)
    
    
    
admin.site.register(NoteBookPage, NoteBookPageAdmin)
admin.site.register(Category)
admin.site.register(Tag)