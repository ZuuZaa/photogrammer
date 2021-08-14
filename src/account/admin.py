from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.models import CustomUser


@admin.register(CustomUser)
class AccountAdmin(BaseUserAdmin):

    list_display = ['email', 'first_name', 'last_name','date_joined']
    list_filter = ['email', 'first_name', 'last_name']
    readonly_fields = ['date_joined','slug']

    fieldsets = (
        ('Personal info', {'fields': ('email', 'first_name', 'last_name','date_joined','slug')}),
        ('Activity', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        ('Personal info', {'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}),
        ('Activity', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    search_fields = ['email', 'first_name', 'last_name']
    ordering = []
    filter_horizontal = []
