# FROM python:3.8
FROM python:3.8-alpine

WORKDIR /app

COPY . .

ENV PYTHONUNBUFFERED=1

RUN \
    apk add bash && \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps