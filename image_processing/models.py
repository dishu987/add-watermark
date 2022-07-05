from django.db import models
from .utils import get_watermark_image
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.
FLAG_CHOICES= (
    ('0', '0'),
    ('1', '1'),
)
class Upload(models.Model):
    image = models.ImageField(upload_to='images')
    watermark = models.ImageField(upload_to='watermarks')
    flag = models.CharField(max_length=50, choices=FLAG_CHOICES)
    alpha = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)

