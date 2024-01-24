# django-samples
A simple sample implementation of a Django program I created for myself.

自分用に備忘録として作成したシンプルなDjangoプロジェクト。

# Index
- [【Django備忘録】django-environを使って機密情報を別ファイルで管理する](https://qiita.com/sho-gun/items/3c6db701fe326bee5ca4)
  - [sample_project/sample_project/settings.py](https://github.com/sho-gun/django-samples/blob/main/sample_project/sample_project/settings.py)
  - [sample_project/.env](https://github.com/sho-gun/django-samples/blob/main/sample_project/.env)
- Django+jQueryでプログレスバーを表示しながらファイルをアップロードする
  - [sample_project/file_upload](https://github.com/sho-gun/django-samples/tree/main/sample_project/file_upload)

# Quick start
```bash
#!/bin/bash
pip3 install -r requirements.txt

cd sample_project
python3 manage.py migrate

python3 manage.py runserver
```
-> http://localhost:8000/
