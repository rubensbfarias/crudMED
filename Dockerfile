FROM python:3.9.13-alpine3.15
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

WORKDIR /workspace

COPY requirements.txt .

RUN \
    pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

USER root
RUN apk --purge del .build-deps

COPY . .

ENTRYPOINT ["./docker-entrypoint.sh"]
