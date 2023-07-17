from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here

class Post(models.Model):
    title = models.CharField(max_length=500, unique=True)
    body = models.TextField()
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ForeignKey("Category", on_delete=models.DO_NOTHING)
    header_image = models.ImageField()
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category (models.Model):
    name = models.CharField(max_length=500, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):

        return self.name

