from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'titulo', 'author',
        'fecha_creacion', 'publicado'
    ]
    search_fields = [
        'titulo'
    ]
    list_filter = [
        'publicado'
    ]

admin.site.register(Post, PostAdmin)