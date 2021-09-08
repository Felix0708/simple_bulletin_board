from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(upload_to='origins/', blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(250, 250)],
        format='JPEG',
        options={'quality': 90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
