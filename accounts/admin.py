from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Referral,LoginHistory

User = get_user_model()

admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):

    list_display = ["email","full_name", "username"]
    list_filter = ["is_active"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            ("Personal info"),
            {
                "fields": (
                    "country_of_residence",
                    "citizenship",
                    "gender",
                    "zipcode",
                    "city",
                    "place_of_birth",
                    "date_of_birth",
                    "phone",
                    "address",
                    
                    "state",
                    "account_opening_reason",
                    "local_currency",
                    "referral",
                    "referral_bonus",
                )
            },
        ),
        (("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
        (
            ("Balance"),
            {"fields": ("balance", "total_deposit", "total_withdraw", "username")},
        ),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Referral)
admin.site.register(LoginHistory)
