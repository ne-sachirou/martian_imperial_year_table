FROM python:3-alpine

SHELL ["/bin/ash", "-ex", "-o", "pipefail", "-c"]

ENV FLASK_APP=web_main.py \
    FLASK_ENV=development \
    PIPENV_VENV_IN_PROJECT=1

WORKDIR /data
VOLUME /data

COPY package.json package-lock.json Pipfile Pipfile.lock ./
RUN apk add --no-cache -t .build-deps \
    build-base \
    linux-headers \
    nodejs \
    npm \
    pcre-dev \
    python3-dev \
 && apk add --no-cache -t .runtime-deps \
    git \
    the_silver_searcher \
 && pip install pipenv \
 && wget -O /usr/local/bin/container-structure-test https://storage.googleapis.com/container-structure-test/latest/container-structure-test-linux-amd64 \
 && chmod +x /usr/local/bin/container-structure-test \
 && wget -O /usr/local/bin/hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64 \
 && chmod +x /usr/local/bin/hadolint \
 && rm -rf /var/cache/apk/*

EXPOSE 5000

CMD ["pipenv", "run", "flask", "run", "-h", "0.0.0.0"]