# syntax=docker/dockerfile:1.4


FROM --platform=$BUILDPLATFORM python:slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends gettext
EOF

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt --no-cache-dir

COPY . .

