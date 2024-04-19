from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('deleted_at',)
    pass

admin.site.register(Category,CategoryAdmin)