# syntax=docker/dockerfile:1.4

FROM node:lts-alpine AS development
# NODE_VERSION=20.16.0
# ALPINE_VERSION=3.20.2
# YARN_VERSION=1.22.22
# NPM_VERSION=10.8.1

WORKDIR /app

COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json

RUN npm ci

COPY . /app

ENV CI=true
ENV PORT=80


CMD [ "npm", "start" ]

FROM development as dev-envs
RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends git
EOF

RUN <<EOF
useradd -s /bin/bash -m vscode
groupadd docker
usermod -aG docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
CMD [ "npm", "start" ]

FROM development AS builder
RUN npm run build

FROM nginx:alpine
# TODO: need to use .nginx/nginx.conf or react optimized image
COPY --from=builder /app/build /usr/share/nginx/html