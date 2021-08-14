from django.contrib import admin
from account.models import CustomUser
from django.db import models

from photo.models import Photo


@admin.register(Photo)
class Photo_Admin(admin.ModelAdmin):
    lfilter = ['user']
    filter_horizontal = ['shared_users']
    readonly_fields = []