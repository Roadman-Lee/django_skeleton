from django.contrib import admin

from accounts.models import UserProfile, User, Hobby


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    filter_horizontal = ("hobby",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "join_date",
    )
    list_display_links = (
        "username",
        "email",
        "join_date",
    )
    list_filter = ("join_date",)
    readonly_fields = ("join_date",)
    search_fields = (
        "username",
        "email",
        "join_date",
    )
    fieldsets = (
        (
            "info",
            {
                "fields": (
                    "username",
                    "email",
                    "join_date",
                )
            },
        ),
        (
            "permissions",
            {
                "fields": (
                    "is_admin",
                    "is_active",
                )
            },
        ),
    )
    inlines = (UserProfileInline,)


# UserProfileInline으로 대체하여 주석처리
# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = (
#         "fullname",
#         "nickname",
#         "zipcode",
#         "address",
#         "introduction",
#         "birthday",
#     )
#     list_display_links = (
#         "fullname",
#         "nickname",
#         "zipcode",
#         "address",
#         "introduction",
#         "birthday",
#     )
#     list_filter = ("address",)
#     search_fields = (
#         "fullname",
#         "nickname",
#         "zipcode",
#         "address",
#         "introduction",
#         "birthday",
#     )
#
# @admin.register(Hobby)
# class HobbyAdmin(admin.ModelAdmin):
#     list_display = ("id", "name",)
#     list_display_links = ("id", "name",)
#     search_fields = ("id", "name",)