# 初期状態
# from django.db import models

# # Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone

# オブジェクト
class Post(models.Model): # 引数の内容はDjangoにDBに保存するものを教える
    # プロパティ群
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # ForeignKey は1対多のモデルをリンクさせる，設定は子モデル側に
    title = models.CharField(max_length=200) # CharField は他に無効な文字列設定もできる
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title