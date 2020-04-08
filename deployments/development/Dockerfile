FROM python:3-alpine

SHELL ["/bin/ash", "-ex", "-o", "pipefail", "-c"]

WORKDIR /mnt
VOLUME /mnt

EXPOSE 5000

ENV PATH=/root/.poetry/bin:$PATH

RUN apk add --no-cache -t .build-deps \
    curl \
 && apk add --no-cache -t .runtime-deps \
    build-base \
    git \
    inotify-tools \
    libffi-dev \
    linux-headers \
    nodejs \
    npm \
    openssl-dev \
    pcre-dev \
    python3-dev \
    rsync \
    the_silver_searcher \
 && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
 && apk del --purge .build-deps \
 && rm -rf /var/cache/apk/*

COPY package.json package-lock.json poetry.lock poetry.toml pyproject.toml ./
RUN poetry install \
 && npm ci \
 && mv node_modules /tmp

ENTRYPOINT ["./deployments/development/entrypoint.sh"]
