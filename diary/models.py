from django.db import models
from django.contrib.auth.models import User
from pathlib import Path
import uuid
# id、タイトル、本文、日記の日付、作成日時、更新日時
class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='投稿者')
    title = models.CharField(max_length=100, verbose_name='タイトル')
    body = models.TextField(max_length=2000, verbose_name='本文')
    page_date = models.DateField(verbose_name='日時')
    picture = models.ImageField(upload_to='diary/picture/', blank=True, null=True, verbose_name='写真')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')  # データが初めて作成されたその時の日時を保存
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')  # データが保存、更新されるたびにその時の日時を保存

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        picture = self.picture
        super().delete(*args, **kwargs)
        if picture:
            Path(picture.path).unlink(missing_ok=True)