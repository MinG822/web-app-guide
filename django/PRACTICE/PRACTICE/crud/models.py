from django.db import models

# Create your models here.

class Crud(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    image_url = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)