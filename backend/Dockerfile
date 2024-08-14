# syntax=docker/dockerfile:1.4


FROM --platform=$BUILDPLATFORM python:slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends make
apt-get clean && rm -rf /tmp/* /var/tmp/*
EOF

RUN python -m pip install --upgrade pip

COPY requirements requirements

RUN python -m pip install -r requirements/dev.txt --no-cache-dir

# COPY Makefile Makefile
# RUN python -m pip install -r requirements/pip-tools.txt --no-cache-dir
# RUN make dev-requirements

COPY . .
