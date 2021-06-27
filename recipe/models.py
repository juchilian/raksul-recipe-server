from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    making_time = models.CharField(max_length=100, blank=False, null=False)
    serves = models.CharField(max_length=100, blank=False, null=False)
    ingredients = models.CharField(max_length=300, blank=False, null=False)
    cost = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)