from django.contrib import admin
from .models import Review, Webtoon, Company, ThemeTag


admin.site.register(Company)
admin.site.register(ThemeTag)
@admin.register(Webtoon)
class WebtoonAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'is_recommended')
    list_filter = ('is_recommended', 'status', 'company')
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('webtoon','created_at')
    list_filter = ('webtoon',)
