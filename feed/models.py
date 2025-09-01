from django.db import models
from sorl.thumbnail import ImageField
import os

class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    image = ImageField(upload_to='posts/images/', blank=True, null=True)
    file = models.FileField(upload_to='posts/files/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # If a file is uploaded but no image, use default placeholder image
        if self.file and not self.image:
            self.image = 'defaults/123FC85F-3BD5-4E7A-9EB5-ADCB94EA3184_1_201_a.jpeg'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text