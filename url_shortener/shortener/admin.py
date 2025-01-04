from django.contrib import admin
from .models import ShortURL
# Register your models here.


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'created_at')
    list_filter = ('created_at',)
