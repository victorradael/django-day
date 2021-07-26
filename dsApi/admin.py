from django.contrib import admin
from .models import Athlete

class Athlets(admin.ModelAdmin):
    list_display = ('id', 'name', 'height', 'weight', 'age')
    list_display_links = ('id', 'name')
    search_fields = ( 'name',)
    list_per_page=20

admin.site.register(Athlete, Athlets)
