# ※ref
# https://qiita.com/nokonoko_1203/items/242367a83c313a5e46bf

# TODO: beanstalkが3.8対応してないが、ひとまず3.8で動かす
FROM python:3.8-alpine

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1
# ソース格納先（右記エラー対応・・・ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?）
ENV PYTHONPATH /usr/src/app

# Pipenvをインストール
RUN pip install --upgrade pip \
&& pip install pipenv

# psycopg2インストール用パッケージの追加
RUN apk update && apk add --no-cache --virtual .build-deps postgresql-dev gcc python3-dev musl-dev libxml2-dev libxslt-dev

# ソースをコピー
# Pipfile、Pipfile.lockもコピーされる
COPY . /usr/src/app/
# pipfileからパッケージをインストールしてDjango環境を構築
RUN pipenv install 
# --skip-lock --system --dev

# psycopg2インストール用パッケージの削除
RUN apk del --no-cache .build-deps

