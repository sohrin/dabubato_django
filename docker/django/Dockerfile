# ※ref
# https://qiita.com/nokonoko_1203/items/242367a83c313a5e46bf

# TODO: beanstalkが3.8対応してないが、ひとまず3.8で動かす
# MEMO: Aplineだとビルドに時間がかかるため、Ubuntuを利用
FROM python:3.8

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

# psycopg2インストール＆不要ファイル削除
###RUN apk update && apk add --no-cache --virtual .build-deps postgresql-dev gcc python3-dev musl-dev libxml2-dev libxslt-dev
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# ソースをコピー（Pipfile、Pipfile.lockもコピーされる）
COPY . /usr/src/app/
# pipfileからパッケージをインストールしてDjango環境を構築
RUN pipenv install

# dockerize
ENV DOCKERIZE_VERSION v0.6.1
RUN apt-get update && apt-get install -y wget \
 && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# TODO: 何故か動作しなかったためdocker-compose側にコマンドを記載した。時間があれば調査する。
#CMD ["dockerize", "-timeout", "300s", \
#     "-wait", "tcp://postgres:5432", \
#     "-wait-retry-interval", "5s", \
#     "pipenv", "run", "python", "manage.py" "migrate", \
#     "&&" \
#     "pipenv", "run", "python", "manage.py" "runserver", "0.0.0.0:8000"]