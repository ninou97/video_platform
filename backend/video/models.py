from django.db import models
from django.conf import settings # Для ссылки на AUTH_USER_MODEL

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/') # Файлы видео будут храниться в media/videos/
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True) # Если нужны превью
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='videos')
    upload_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-upload_date'] # Сортировка по дате загрузки