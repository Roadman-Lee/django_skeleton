from django.contrib import admin

from blog.models import Article, Category, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "author",
        "title",
        "article",
        "is_public",
        "created_at",
        "updated_at",
    )
    list_display_links = ("pk", "author", "title", "article")
    list_filter = ("is_public",)
    search_fields = ("author", "title", "article")
    filter_horizontal = ("tag_set",)
    fieldsets = (
        (
            "Article",
            {
                "fields": (
                    "author",
                    "title",
                    "article",
                    "category_set",
                    "tag_set",
                )
            },
        ),
        (
            "Disclosure status",
            {
                "fields": (
                    "is_public",
                )
            },
        ),
    )


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ["id", "name", "description"]
#     list_display_links = ["id", "name", "description"]
#     search_fields = ["id", "name", "description"]
#
#
# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ["id", "name"]
#     list_display_links = ["id", "name"]
#     search_fields = ["id", "name"]
