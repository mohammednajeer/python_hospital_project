from django.db import models

# Create your models here.
class DEpartments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_decription =models.TextField()