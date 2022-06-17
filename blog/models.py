from django.db import models

from app import settings


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author"
    )
    title = models.CharField(max_length=255)
    article = models.TextField()
    photo = models.ImageField(blank=True, upload_to="instagram/post/%y/%m/%d")
    category_set = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, related_name="category_set", blank=True
    )
    tag_set = models.ManyToManyField(to=Tag, blank=True)
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]
