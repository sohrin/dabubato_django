# dabubato_django
Double Battle Management System (Django)

## ref
* Windows + Python + PipEnv + Visual Studio Code でPython開発環境
https://qiita.com/youkidkk/items/b674e6ace96eb227cc28

* [Django] プロジェクト構成のベストプラクティスを探る - １．設定ディレクトリの名前を変更する
https://qiita.com/okoppe8/items/6227d753185fccf21c75

* 『超入門』Djangoで作る初めてのウェブアプリケーション Part3（プロジェクト, アプリ）
https://note.com/takuya814/n/nbee813cecabb

## install
* python3
* pipenv
* vscode

## project init
1. GitHubでリポジトリ作成しgit clone
2. vscodeでフォルダを開き、ターミナルを開く
3. 以下コマンドを実行
``` command
pipenv --python 3.8
pipenv install Django
pipenv shell
django-admin startproject config .
python manage.py runserver
```

## project clone
1. 以下コマンドを実行
```
git clone
pipenv install
pipenv shell
python manage.py runserver
```

## todo
* プロジェクト直下のdb.sqlite3は必要？
* RestAPI
* DBアクセス（ORM）
* ログイン認証（画面）
* セッション
* JWT認証（API）
* HTTPクライアント
* SPA