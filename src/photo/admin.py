from django.contrib import admin
from django.db import models

from photo.models import Photo


@admin.register(Photo)
class Photo_Admin(admin.ModelAdmin):
    filter = ['user']
    filter_horizontal = ['shared_users']
    readonly_fields = []