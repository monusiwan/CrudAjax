from django.db import models

# Create your models here.
class Stduent(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to="images")
    mobile = models.CharField(max_length=15)