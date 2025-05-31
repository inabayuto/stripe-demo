# 開発用ステージ
FROM python:3.11.9-slim-bookworm AS developer

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    wget \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .