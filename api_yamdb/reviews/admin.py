from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title, User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'description', 'category', 'rating')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'text', 'pub_date', 'score')
    empty_value_display = '-пусто-'
    search_fields = ('text',)
    list_filter = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'author', 'text', 'pub_date')
    empty_value_display = '-пусто-'
    search_fields = ('text',)
    list_filter = ('review',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(User)
