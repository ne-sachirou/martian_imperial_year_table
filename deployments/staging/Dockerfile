FROM python:3-alpine AS builder

SHELL ["/bin/ash", "-ex", "-o", "pipefail", "-c"]

WORKDIR /mnt

COPY package.json package-lock.json poetry.lock poetry.toml pyproject.toml ./
RUN apk add --no-cache -t .build-deps \
    build-base \
    curl \
    linux-headers \
    nodejs \
    npm \
    pcre-dev \
    python3-dev \
 && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
 && poetry install --no-dev \
 && npm ci \
 && rm -rf /var/cache/apk/*

COPY ui_main.py ./
COPY imperial_calendar/ imperial_calendar/
COPY static/ static/
COPY ui/ ui/
RUN mkdir -p static/css static/js \
 && cp node_modules/bulma/css/* static/css/ \
 && poetry run transcrypt -b -m -n ui_main.py \
 && mv __target__/* static/js/ \
 && rm -rf "$(poetry --venv)" \
 && poetry install


FROM python:3-alpine

SHELL ["/bin/ash", "-ex", "-o", "pipefail", "-c"]

ENV FLASK_ENV=production

WORKDIR /mnt

RUN apk add --no-cache -t .build-deps \
    curl \
    shadow \
 && apk add --no-cache -t .runtime-deps \
    pcre \
 && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
 && useradd uwsgi --no-create-home --user-group \
 && apk del --purge .build-deps \
 && rm -rf /var/cache/apk/*

COPY --from=builder /mnt/.venv/ .venv/
COPY --from=builder /mnt/static/ static/
COPY poetry.lock poetry.toml pyproject.toml web_main.py web.yml ./
COPY imperial_calendar/ imperial_calendar/
COPY templates/ templates/

EXPOSE 5000 9191
ENTRYPOINT ["poetry", "run", "uwsgi", \
            "--die-on-term", \
            "--master", \
            "--uid", "uwsgi", \
            "--virtualenv", ".venv"]
CMD ["--callable", "app", \
     "--http", ":5000", \
     "--processes", "2", \
     "--stats", "127.0.0.1:9191", \
     "--threads", "2", \
     "--wsgi-file", "web_main.py"]
