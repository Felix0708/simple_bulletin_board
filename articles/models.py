from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

CATEGORY_CHOICES = [
    ('자유', '자유'),
    ('가입인사', '가입인사'),
    ('질문', '질문'),
    ('정보', '정보'),
    #뒤에 사용자가 보게 될 값, 앞은 실제 데이터베이스 보이는 값
]

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    content = models.TextField()
    image = models.ImageField(upload_to='origins/', blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(250, 250)],
        format='JPEG',
        options={'quality': 90},
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
