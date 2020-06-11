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
* HTTPクライアント
* JWT認証（API）
<https://auth0.com/blog/jp-building-modern-applications-with-django-and-vuejs/#Django---Vue-js-------------Auth0------------------------->
* SPA（Vue.js直接組み込みに留めておくか）
<https://scrapbox.io/vue-yawaraka/Vue%E3%81%AECDN%E7%89%88%E3%82%92%E4%BD%BF%E3%81%8A%E3%81%86>
<https://scrapbox.io/vue-yawaraka/CDN%E7%89%88%E3%81%A7%E5%A4%A7%E3%81%8D%E3%81%AA%E3%82%A2%E3%83%97%E3%83%AA%E4%BD%9C%E3%82%8C%E3%82%8B%E3%81%AE%EF%BC%9F>
<https://qiita.com/takanorip/items/d1e8618800d951780f4b>
<https://nmomos.com/tips/2019/07/17/django-vuejs-1/>
<https://qiita.com/kawaMk4/items/89b18c608dc7dd2b946b>
<https://qiita.com/gsk3beta/items/2c237d1434b06e9ebf8b>
<https://akiyoko.hatenablog.jp/entry/2019/09/17/123351>
<https://medium.com/@kaizumaki/django-drf-vue-vuetify-824083717f15>
<https://medium.com/@oikawa/solved-binding-django-and-vuejs-9e3e00f8ddb4>
<https://nomaps.io/2020/02/27/django%E3%81%AEmpa%E3%81%AE%E3%83%95%E3%83%AD%E3%83%B3%E3%83%88%E3%82%A8%E3%83%B3%E3%83%89%E3%81%A7vue-jsvuetify-js/>

* コンテナ化
* デプロイ
<https://docs.aws.amazon.com/ja_jp/elasticbeanstalk/latest/dg/create-deploy-python-django.html>
<https://dev.classmethod.jp/articles/aws-elastic-beanstalk-for-docker-1/>
<https://recipe.kc-cloud.jp/archives/16692>
<https://qiita.com/soreiyu52/items/ec25f14d5ebbf15fe6ea>
<https://qiita.com/Ken227/items/d3a569c127cfe1ea5a83>
<https://qiita.com/kyhei_0727/items/e0eb4cfa46d71258f1be>
<https://roy-n-roy.github.io/Docker/Django/>
<https://sleepless-se.net/2018/06/12/dockerdjango%E3%82%92%E7%84%A1%E6%96%99%E3%81%A7https%E5%8C%96%E3%81%97%E3%81%A6%E7%B0%A1%E5%8D%98%E3%81%AB%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/>
<http://pythonskywalker.hatenablog.com/entry/2016/11/17/152830>
