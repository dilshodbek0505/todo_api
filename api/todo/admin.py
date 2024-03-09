from django.contrib import admin

from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "auth", "description", "is_done", "created", "updated")
    list_display_links = ("id", "name", "auth")
