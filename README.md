# dabubato_django
Double Battle Management System (Django)

## 懸念メモ
* Djangoのモデルは複数プライマリーキーに対応していない。

## TODO
* モデルに__str__メソッドを追加
<https://docs.djangoproject.com/ja/3.0/intro/tutorial02/>
* PythonのJavaDoc的なもの
* コード静的チェック
* 型チェック
* テーブル結合
<https://qiita.com/chokosuki4400/items/b517a43172e2e0c71de0>
<http://wpress.biz/django/2017/02/25/django%EF%BC%9A%E5%A4%96%E9%83%A8%E3%82%AD%E3%83%BC%E3%81%AB%E3%82%88%E3%82%8B%E3%83%86%E3%83%BC%E3%83%96%E3%83%AB%E7%B5%90%E5%90%88%E3%82%92%E3%81%A4%E3%81%8B%E3%81%A3%E3%81%A6%E3%83%87%E3%83%BC/>
<https://teratail.com/questions/219332>
<https://qiita.com/shimayu22/items/1c0d9f0365ce6cc6488f>

## TODO(二軍)
* SP・DP・DBで1つのMstMusicとする

## memo
* preview Markdown：［Ctrl］＋［K］→［V］
* eb logs
* eb ssh (input keypair pass)
* VSCode Python Djangoの問題（エラー・警告）に対応する方法
<https://wonwon-eater.com/vscode-python-django-lint/>
* VS Codeのsettings.jsonの開き方
<https://qiita.com/y-w/items/614843b259c04bb91495>
* html5テンプレ
<https://www.webprofessional.jp/a-basic-html5-template/>
<https://qiita.com/storeG/items/80bcea89caa46e240a64>

## python memo
* 【Python入門】dictionary（辞書）の使い方。基本と応用
<https://www.sejuku.net/blog/24122>
* 【Python入門】if文の論理演算子notの使い方をやさしく解説！
<https://www.sejuku.net/blog/65070>
* How do I get a python program to do nothing?
<https://stackoverflow.com/questions/19632728/how-do-i-get-a-python-program-to-do-nothing/19632742>
* python 配列基礎はこれで完璧！便利なメソッド多数紹介
<https://udemy.benesse.co.jp/development/web/python-list.html>
* Python Tips： switch 文を使いたい
<https://www.lifewithpython.com/2018/08/python-switch-case-statement.html>
* Pythonで自作の例外を発生させるraiseの使い方を現役エンジニアが解説【初心者向け】
<https://techacademy.jp/magazine/22124>
* Pythonでヌルオブジェクトの比較
<https://qiita.com/tortuepin/items/44fdb63cc82dfd260575>
* Python 文字列を切り取る[]
<https://pg-chain.com/python-str-substring>

## Django memo
* モデル (Model) - データアクセスの基礎
<https://python.keicode.com/django/model-data-access-basics.php>



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
* PostgreSQL

## install (for deploy)
* aws-mfa(pip install aws-mfa)
インストール時に以下エラーが出たが動作に問題なかった・・・ことはなく、eb init時にエラーが出た。pip install awsebcliをインストールし直せば、aws-mfaもebも動いたので、先にaws-mfaをインストールすべき。
```
ERROR: awsebcli 3.18.1 has requirement botocore<1.16,>=1.15, but you'll have botocore 1.17.1 which is incompatible.
```
* awsebcli(pip install awsebcli)

## CREATE DATABASE(PostgreSQL)
<https://qiita.com/shigechioyo/items/9b5a03ceead6e5ec87ec>
1. 以下コマンドを実行(仮想環境から抜けている状態から)
``` command
psql -U postgres
CREATE DATABASE dabubato_db;
CREATE USER dabubato_user WITH PASSWORD 'dabubato_pass';
ALTER ROLE dabubato_user SET client_encoding TO 'utf8';
ALTER ROLE dabubato_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE dabubato_user SET timezone TO 'Asia/Tokyo';
GRANT ALL PRIVILEGES ON DATABASE dabubato_db TO dabubato_user;
\q
```
2. pg_hba.confを確認し、Peer認証許可の場合はパスワード認証(md5)許可に変更しPostgreSQLを再起動。
3. migrateをやり直す場合、以下を実施しデータベースを再作成、migrationsフォルダ配下の履歴pyファイルを削除してから、makemigrations、migrate、createsuperuserをやり直すこと。
``` command
psql -U postgres
DROP DATABASE dabubato_db;
CREATE DATABASE dabubato_db;
GRANT ALL PRIVILEGES ON DATABASE dabubato_db TO dabubato_user;
\q
```

## define MODELS
<https://docs.djangoproject.com/ja/3.0/topics/db/models/>
<https://docs.djangoproject.com/ja/3.0/ref/models/fields/>
<https://32imuf.com/django/model/>
<https://stackoverflow.com/questions/18934149/how-can-i-use-postgresqls-text-column-type-in-django>
<https://ti-tomo-knowledge.hatenablog.com/entry/2018/05/24/083429>
<https://eiry.bitbucket.io/tutorials/tutorial/models.html>
<https://stackoverflow.com/questions/1545645/how-to-set-django-model-field-by-name/1545668>
<https://qiita.com/ekzemplaro/items/377adfb74fa3517f98df>
<https://teratail.com/questions/227263>
<https://www.programiz.com/python-programming/datetime/current-datetime>
<http://www.denzow.me/entry/2017/12/23/150501>
<https://qiita.com/ekzemplaro/items/f57f3cac56cbab7d6ac8>
<https://yaruki-strong-zero.hatenablog.jp/entry/python3_datetime_timezone_pytz>
<https://opendata-web.site/blog/entry/22/>
<https://qiita.com/shinno21/items/a2987d8f1e1df4f38114>
1. appフォルダ/models.pyのモデル定義を編集
2. 以下コマンドを実行(仮想環境から抜けている状態から)
``` command
python manage.py makemigrations
python manage.py migrate
```

## project clone and run (python)
1. リポジトリをgit clone
2. vscodeのsetting.jsonに以下を追加（ctrl+, -> 右上のOpen Settings(JSON)アイコン）
```
"python.linting.pylintArgs": [
    "--load-plugins=pylint_django",
]
```
3. vscodeでフォルダを開き、ターミナルを開く
4. CREATE DATABASE(PostgreSQL)作業の実施
5. 以下コマンドを実行(仮想環境から抜けている状態から)
```
pipenv install
pipenv shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## project clone and run (docker-compose)
<https://qiita.com/nokonoko_1203/items/242367a83c313a5e46bf>
<https://shimakaze.hatenablog.com/entry/2016/01/19/165828>
<https://github.com/psycopg/psycopg2/issues/684>
<https://stackoverflow.com/questions/49631146/how-do-you-add-a-path-to-pythonpath-in-a-dockerfile>

<https://stackoverflow.com/questions/57164656/could-not-install-the-packages-using-pipenv-when-using-docker>
1. TODO: 後で書く


## project init
1. GitHubでリポジトリ作成しgit clone
2. vscodeでフォルダを開き、ターミナルを開く
3. 以下コマンドを実行(仮想環境から抜けている状態から)
``` command
pipenv --python 3.8
pipenv install Django
pipenv shell
django-admin startproject config .
python manage.py runserver
```

## project first webapp
<https://docs.djangoproject.com/ja/3.0/intro/tutorial01/>
<https://qiita.com/shigechioyo/items/b7980e4f5dc62c51d2cb>
1. 以下コマンドを実行(仮想環境から抜けている状態から)
``` command
pipenv shell
django-admin startapp dabubato
```
2. dabubato/views.py（MVCのController）にメソッド追加
3. dabubato/urls.pyを作成しURLマッピングを追加
4. config/urls.pyにdabubato/urls.pyをインクルード
5. runserver後に以下にアクセス
http://127.0.0.1:8000/dabubato/

## project first batch(custom command)
<https://qiita.com/retasu0/items/5bd4bc9080343f9fe59f>
<https://stackoverflow.com/questions/2190539/django-custom-command-not-found>
1. django-admin startappコマンド実行によりできたdabubatoフォルダに「management/commands/サブコマンド名.py」を作成
2. python manage.py サブコマンド名

## setting DATABASE
<https://qiita.com/shigechioyo/items/9b5a03ceead6e5ec87ec>
1. 以下コマンドを実行(仮想環境から抜けている状態から)
``` command
pipenv install psycopg2-binary
```
2. config/setting.pyのDATABASES設定を修正
3. 以下コマンドを実行(仮想環境から抜けている状態から)
``` command
pipenv shell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
※ヒント：sから始まる
```

## scraping
<https://qiita.com/aocattleya/items/2eab8ad744d9a28fb9ce>
<http://rongonxp.hatenablog.jp/entry/2018/02/01/000816>
<https://blog.ikedaosushi.com/entry/2019/09/15/162445>
<https://github.com/miyakogi/pyppeteer/issues/66>
<https://stackoverflow.com/questions/49268423/requests-html-enconding-error>
<https://github.com/psf/requests-html/issues/85>
<https://gammasoft.jp/blog/how-to-download-web-page-created-javascript/>
1. 以下コマンドを実行(仮想環境から抜けている状態から)
``` command
↑JavaScriptでレンダリングされるサイトをスクレイピングしたいので↓を使う
pipenv install requests-html
2. music-mst-mainte.pyにガリガリコーディング


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
1.以下コマンドを実行(仮想環境から抜けている状態から)
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
