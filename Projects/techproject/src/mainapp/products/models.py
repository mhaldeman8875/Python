from django.db import models

# Create your models here.
class Product(models.Model):
  type = models.CharField(max_length=60)
  name = models.models.CharField(max_length=50, default="", blank=True, null=False)
  description = models.TextField(max_length=100, default="", blank=True)
  price = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
  image = models.CharField(max_length=255, default="", blank=True,)