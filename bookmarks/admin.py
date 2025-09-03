from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Folders
from .models import Groups
from .models import Bookmarks

class BookmarksAdmin(admin.ModelAdmin):
    list_display = ("id", "group", "folder", "name", "show_url")

    @admin.display(description="URL")
    def show_url(self, obj):
        return format_html("<a href='{url}' target='_blank'  rel='noopener noreferrer'>{url}</a>", url=obj.url)

class GroupsAdmin(admin.ModelAdmin):
    list_display = ("id", "group", "description")

class FoldersAdmin(admin.ModelAdmin):
    list_display = ("id", "group", "parent_id", "name")

admin.site.register(Folders, FoldersAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(Bookmarks, BookmarksAdmin)

