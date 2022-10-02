from django.db import models


# Create your models here.
class OriginalImage(models.Model):
    image = models.ImageField(upload_to='original/', null=True)


class Images(models.Model):
    original_img = models.ForeignKey(OriginalImage, on_delete=models.CASCADE)
    grayscale_img = models.ImageField(upload_to='grayscale/', null=True)
    sketch_img = models.ImageField(upload_to='sketch/', null=True)
