# Docker で作る postgres 環境
# https://crudzoo.com/blog/docker-postgres

# ※Amazon RDSは2020-06-16時点では11.6まで対応
FROM postgres:11.7-alpine
ENV LANG ja_JP.utf8

# 初期設定（DB・ロール作成のみDockerfileで行い、マイグレーションはDjangoにて実施）
COPY docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/