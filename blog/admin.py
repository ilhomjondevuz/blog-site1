from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at', 'updated_at')
    search_fields = ('title',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('author', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'photo',
                'author',
                'content',
                'created_at',
                'updated_at',
            )
        })
    )
    add_fieldsets = (
        (None, {
            'fields': (
                'title',
                'author',
                'content',
                'photo'
            )
        })
    )

admin.site.register(Post)