from django.contrib import admin

from .models import Car, Comment

admin.site.empty_value_display = 'Не задано'


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 2


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'car',
        'created_at',
    )
    search_fields = ('author', 'car')
    list_filter = ('created_at',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = (
        CommentInline,
    )
    list_display = (
        'make',
        'model',
        'year',
        'updated_at',
        'owner',
    )
    search_fields = ('make', 'model')
    list_filter = ('created_at',)
