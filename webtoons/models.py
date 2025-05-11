from django.db import models

# Create your models here.
import uuid
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ThemeTag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Webtoon(models.Model):
    STATUS_CHOICES = [
        ('serializing', '연재 중'),
        ('completed', '완결'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    link_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, related_name='webtoons')
    themes = models.ManyToManyField(ThemeTag, related_name='webtoons')
    is_recommended = models.BooleanField(default=False)  # ✅ NEW
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    webtoon = models.OneToOneField('Webtoon', on_delete=models.CASCADE, related_name='review')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.webtoon.title}"
