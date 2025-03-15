from django.db import models
from .helpers import generate_unique_short_code

class ShortURL(models.Model):
    original_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=6, unique=True, default=generate_unique_short_code)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"


