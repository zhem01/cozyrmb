from django.contrib import admin
from .models import ProductCategory, Option, SlideBanner

class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "base_price_usd", "base_price_khr")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [OptionInline]

@admin.register(SlideBanner)
class SlideBannerAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
