# dabubato_django
Double Battle Management System (Django)

## memo
* preview Markdown：［Ctrl］＋［K］→［V］
* eb logs
* eb ssh (input keypair pass)

## ref
* Windows + Python + PipEnv + Visual Studio Code でPython開発環境
https://qiita.com/youkidkk/items/b674e6ace96eb227cc28

* [Django] プロジェクト構成のベストプラクティスを探る - １．設定ディレクトリの名前を変更する
https://qiita.com/okoppe8/items/6227d753185fccf21c75

* 『超入門』Djangoで作る初めてのウェブアプリケーション Part3（プロジェクト, アプリ）
https://note.com/takuya814/n/nbee813cecabb

## install (for dev)
* python3(Windows,2020-06-12 -> python-3.8.3-amd64.exe, add PATH, customize -> pip, alluser)]
* update pip(admin cmd -> python -m pip install --upgrade pip)
* pipenv(pip install pipenv, add pipenv to PATH, where pipenv)
* vscode
* vscode extention(ms-python.python)

## install (for deploy)
* aws-mfa(pip install aws-mfa)
インストール時に以下エラーが出たが動作に問題なかった・・・ことはなく、eb init時にエラーが出た。pip install awsebcliをインストールし直せば、aws-mfaもebも動いたので、先にaws-mfaをインストールすべき。
```
ERROR: awsebcli 3.18.1 has requirement botocore<1.16,>=1.15, but you'll have botocore 1.17.1 which is incompatible.
```
* awsebcli(pip install awsebcli)

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
1. リポジトリをgit clone
2. vscodeでフォルダを開き、ターミナルを開く
3. 以下コマンドを実行
```
pipenv install
pipenv shell
python manage.py runserver
```


★★★TODO: 整理、どこまでgit管理すべきか（ebコマンドが.gitignoreに「.elasticbeanstalk」フォルダ配下ファイルを除外する設定を入れてくれるため、git clone時はひとまず(first only)の 3. からやればいいはず）
## deploy to AWS Elastic Beanstalk(first only)
* 参考サイト（一番初めに参考にした）
<https://www.royozaki.net/archives/697>
<https://qiita.com/reflet/items/d4c4a1c3e5a87c9a2ac2>
* 参考サイト（まだあまり見てない）
<https://webcurtaincall.com/articles/7>
<https://qiita.com/soreiyu52/items/ec25f14d5ebbf15fe6ea>
<https://www.hands-lab.com/tech/entry/1567.html>
<https://aws.amazon.com/jp/getting-started/hands-on/deploy-python-application/>
1. 「.ebextensions」フォルダをプロジェクト直下に作成
2. 「.ebextensions/django.config」を以下内容で新規作成(UTF-8,LF)
```
option_settings:
    aws:elasticbeanstalk:container:python:
        WSGIPath: ebdjango/wsgi.py
```
3. aws-mfa認証後に以下を実行（未認証だと「ERROR: The current user does not have the correct permissions. Reason: Operation Denied. The security token included in the request is expired」エラーが発生する）。
```
eb init
→リージョン選択
→アプリ名はデフォルト
→「It appears you are using Python. Is this correct?」にはY（プラットフォームがPythonで正しいことの確認）
→「1) Python 3.7 running on 64bit Amazon Linux 2」
→CodeCommitはいったん未使用のためn
→SSHは念のためしたいのでY、キーペアは新規、dabubato_django_keypairという名前で作成
→パスフレーズを適当に入力
※「WARNING: Uploaded SSH public key for "dabubato_django_keypair" into EC2 for region ap-northeast-1.」と出て終了
★★★TODO: EC2の鍵はどこにできる？★★★

## deploy to AWS Elastic Beanstalk(create from env)
```
1. 以下を実行（参考サイトのような権限エラーは出なかった）
```
eb create dabubato-django-env ★★★TODO: 環境名がURLに載るので、環境名はdabubatoのほうが良かった・・・★★★
```
2. 「Successfully launched environment: dabubato-django-env」出力確認後、以下を実施し、CNAME値を「config/setting.py」のALLOWED_HOSTSに追加。
```
eb status
```
3. 「Successfully launched environment: dabubato-django-env」出力確認後、以下を実施し、CNAME値を「config/setting.py」のALLOWED_HOSTSに追加。★★★TODO: 追加しないとどうなる？★★★
```
eb deploy
eb open
★★★TODO: 「502 Bad Gateway」が表示された。「eb logs」でログを確認したところ、「ModuleNotFoundError: No module named 'application'」と出ていた。★★★
```
4. GOTO 「env already created」

## deploy to AWS Elastic Beanstalk(env already created)
1. pipenv shellからexitしている状態で以下コマンドを実行
```
pipenv run pip freeze > requirements.txt
```

## undeploy to AWS Elastic Beanstalk
1. アプリ削除の場合：【TODO: ？？？】
2. 環境削除の場合：eb terminate

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
