from django.contrib import admin

# Register your models here.
from .models import Post , Category
admin.site.register(Post)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']  # Add 'slug' to the list_display

admin.site.register(Category, CategoryAdmin)
