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

COPY ./entrypoint.sh /app
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["gunicorn", "config.wsgi:application", "--workers", "2", "--timeout", "90","--bind", "0.0.0.0:8000"]