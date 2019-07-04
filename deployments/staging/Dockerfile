FROM python:3-alpine AS builder

SHELL ["/bin/ash", "-ex", "-o", "pipefail", "-c"]

ENV PIPENV_VENV_IN_PROJECT=1

WORKDIR /data

COPY package.json package-lock.json Pipfile Pipfile.lock ./
RUN apk add --no-cache -t .build-deps \
    build-base \
    linux-headers \
    nodejs \
    npm \
    pcre-dev \
    python3-dev \
 && pip install pipenv \
 && pipenv install -d --deploy \
 && npm ci \
 && rm -rf /var/cache/apk/*

COPY ui_main.py ./
COPY imperial_calendar/ imperial_calendar/
COPY ui/ ui/
RUN mkdir -p static/css static/js \
 && cp node_modules/bulma/css/* static/css/ \
 && pipenv run transcrypt -b -k -m -n ui_main.py \
 && mv __target__/* static/js/ \
 && rm -rf "$(pipenv --venv)" \
 && pipenv install --deploy


FROM python:3-alpine

SHELL ["/bin/ash", "-ex", "-o", "pipefail", "-c"]

ENV FLASK_ENV=production \
    PIPENV_VENV_IN_PROJECT=1

WORKDIR /data

RUN apk add --no-cache -t .build-deps \
    shadow \
 && apk add --no-cache -t .runtime-deps \
    pcre \
 && pip install pipenv \
 && useradd uwsgi --no-create-home --user-group \
 && apk del --purge .build-deps \
 && rm -rf /var/cache/apk/*

COPY --from=builder /data/.venv/ .venv/
COPY --from=builder /data/static/ static/
COPY Pipfile Pipfile.lock web_main.py web.yml ./
COPY imperial_calendar/ imperial_calendar/
COPY templates/ templates/

EXPOSE 5000 9191
ENTRYPOINT ["pipenv", "run", "uwsgi", \
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
