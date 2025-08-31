from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        "email",
        "name",
        "is_staff",
        "is_superuser",
    )
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": (
                "email",
                "name",
                "password",
                "is_staff",
                "is_superuser",
            ),
        },
    )


admin.site.register(User, CustomUserAdmin)
