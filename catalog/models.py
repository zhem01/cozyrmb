from django.db import models
from django.utils.text import slugify

class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    base_price_usd = models.DecimalField(max_digits=6, decimal_places=2)
    base_price_khr = models.PositiveIntegerField()
    hero_image = models.ImageField(upload_to="category/hero/", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Option(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="options")
    name = models.CharField(max_length=40)
    extra_usd = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    extra_khr = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("category", "name")

    def __str__(self):
        return f"{self.category.name} – {self.name}"

class SlideBanner(models.Model):
    image = models.ImageField(upload_to="banners/")
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    link_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Banner {self.id}"
