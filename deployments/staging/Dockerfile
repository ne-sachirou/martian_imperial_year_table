FROM python:3-alpine AS builder

SHELL ["/bin/ash", "-ex", "-o", "pipefail", "-c"]

WORKDIR /mnt

ENV PATH=/root/.poetry/bin:$PATH

RUN apk add --no-cache -t .build-deps \
    curl \
 && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
 && apk del --purge .build-deps \
 && rm -rf /var/cache/apk/*

COPY package.json package-lock.json poetry.lock poetry.toml pyproject.toml ./
RUN apk add --no-cache -t .build-deps \
    build-base \
    linux-headers \
    pcre-dev \
    python3-dev \
 && apk add --no-cache -t .runtime-deps \
    nodejs \
    npm \
 && poetry install \
 && npm ci \
 && apk del --purge .build-deps \
 && rm -rf /var/cache/apk/*

COPY ui_main.py ./
COPY imperial_calendar/ imperial_calendar/
COPY static/ static/
COPY ui/ ui/
RUN mkdir -p static/css static/js \
 && cp node_modules/bulma/css/* static/css/ \
 && cp node_modules/create-react-class/create-react-class.js static/js/create-react-class.js \
 && cp node_modules/react-dom/umd/react-dom.production.min.js static/js/react-dom.js \
 && cp node_modules/react-hook-form/dist/react-hook-form.umd.js static/js/react-hook-form.js \
 && cp node_modules/react-router-dom/umd/react-router-dom.js static/js/react-router-dom.js \
 && cp node_modules/react/umd/react.production.min.js static/js/react.js \
 && poetry run transcrypt -b -m -n ui_main.py \
 && mv __target__/* static/js/


FROM python:3-alpine

SHELL ["/bin/ash", "-ex", "-o", "pipefail", "-c"]

WORKDIR /mnt

ENV FLASK_ENV=production \
    PATH=/root/.poetry/bin:$PATH

RUN apk add --no-cache -t .build-deps \
    curl \
    shadow \
 && apk add --no-cache -t .runtime-deps \
    pcre \
 && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
 && useradd uwsgi --no-create-home --user-group \
 && apk del --purge .build-deps \
 && rm -rf /var/cache/apk/*

COPY poetry.lock poetry.toml pyproject.toml ./
RUN apk add --no-cache -t .build-deps \
    build-base \
    linux-headers \
    pcre-dev \
    python3-dev \
 && poetry install --no-dev \
 && apk del --purge .build-deps \
 && rm -rf /var/cache/apk/*

COPY --from=builder /mnt/static/ static/
COPY web_main.py web.yml ./
COPY imperial_calendar/ imperial_calendar/
COPY templates/ templates/

EXPOSE 5000 9191
ENTRYPOINT ["poetry", "run", "uwsgi", \
            "--die-on-term", \
            "--master", \
            "--uid", "uwsgi"]
CMD ["--callable", "app", \
     "--http", ":5000", \
     "--processes", "2", \
     "--stats", "127.0.0.1:9191", \
     "--threads", "2", \
     "--wsgi-file", "web_main.py"]
