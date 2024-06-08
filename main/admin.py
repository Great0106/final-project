from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('deleted_at',)
    list_display = ["name", "description", "created_at", "updated_at"]

class PostAdmin(admin.ModelAdmin):
    exclude = ('deleted_at', 'user')
    list_display = ["title", "created_at", "updated_at", "published", "user"]
    fields = ('title', 'category', 'published', 'content')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)