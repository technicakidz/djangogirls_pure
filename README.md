# Djangogirls_pure

Django girls チュートリアルの見本レポジトリ
https://tutorial.djangogirls.org/ja/

## Usage
### 仮想環境

作成
```
djangogirls_pure$ python3 -m venv .venv
```

起動
```
djangogirls_pure$ source .venv/bin/activate
```

終了
```
(.venv)djangogirls_pure$ deactivate
```

### サーバの起動
DBのマイグレーション
```
djangogirls_pure$ python3 manage.py migrate
```

```
~/djangogirls_pure$ python manage.py runserver
```

### クラウドサーバ設定
pythonanywhereでのヘルパーを利用した設定
```
pa_autoconfigure_django.py https://github.com/technicakidz/djangogirls_pure.git --nuke --branch=master
```
