from django.contrib import admin
from .models import Post

# Post モデルを呼び出し
# サイトに登録する設定を追加
admin.site.register(Post)