from django.db import models


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='')
    def __str__(self):
        return str(self.pk)