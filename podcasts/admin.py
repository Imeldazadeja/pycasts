from django.contrib import admin
from .models import Episod
# Register your models here.

@admin.register(Episod)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("podcast_name", "title", "pub_date")