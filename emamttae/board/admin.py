from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Board, Post


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_date')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'board', 'owner', 'created_date', 'created_week')
    list_filter = ('created_week',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


