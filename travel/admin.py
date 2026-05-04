from django.contrib import admin
from .models import TravelInfo
@admin.register(TravelInfo)
class TravelInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'province', 'rating', 'hot_score', 'comment_count', 'price')
    search_fields = ('name', 'city', 'province')
    list_filter = ('city', 'province')
    list_per_page = 20

