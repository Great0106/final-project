from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    user_id = models.ForeignKey(
        User,
        on_delete = models.RESTRICT
    )
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()
    published = models.BooleanField(default = False)
    user_id = models.ForeignKey(
        User,
        on_delete = models.RESTRICT
    )
    user_id = models.ForeignKey(
        Category,
        on_delete = models.RESTRICT
    )