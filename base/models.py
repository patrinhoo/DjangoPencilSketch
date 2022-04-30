from django.db import models


# Create your models here.
class Images(models.Model):
    id = models.AutoField(primary_key=True)
    original_img = models.ImageField(upload_to='original/', null=True)
    grayscale_img = models.ImageField(upload_to='grayscale/', null=True)
    sketch_img = models.ImageField(upload_to='sketch/', null=True)
