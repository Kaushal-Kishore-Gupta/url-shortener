from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class URL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    original_url = models.CharField(max_length=500)
    shortened_url = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)