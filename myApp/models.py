from django.db import models

# Create your models here.
class URL(models.Model):
    original_url = models.CharField(max_length=500)
    shortened_url = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)