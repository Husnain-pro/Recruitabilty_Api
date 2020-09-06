from django.contrib import admin

from .models import Album,Artist

admin.register(Album,Artist)(admin.ModelAdmin)
