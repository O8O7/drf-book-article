from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BookModel, UserBookModel, UserModel


@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    ordering = ("id",)
    list_display = ("id", "email", "is_staff", "is_active", "last_login", "date_joined")
    search_fields = ("email",)
    list_filter = ("is_staff", "is_superuser", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("権限", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("最終ログイン・登録日時", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_superuser", "is_active"),
            },
        ),
    )


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_at", "updated_at")
    search_fields = ("title", "author")
    ordering = ("-created_at",)
    list_per_page = 30


@admin.register(UserBookModel)
class UserBookModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "book", "status", "updated_at")
    search_fields = ("user__email", "book__title", "book__author", "memo")
    list_filter = ("status", "created_at", "updated_at")
    autocomplete_fields = ("user", "book")
    ordering = ("-updated_at",)
    list_select_related = ("user", "book")
    list_per_page = 50
