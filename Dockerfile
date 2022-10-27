FROM python:3.9.13-alpine3.15
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN \
    adduser -D usr && \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

WORKDIR /workspace
USER usr

COPY --chown=usr:usr requirements.txt .

RUN \
    pip install --user --upgrade pip && \
    pip install --user -r requirements.txt --no-cache-dir

USER root
RUN apk --purge del .build-deps

USER usr
COPY --chown=usr:usr . .

ENTRYPOINT ["docker-entrypoint.sh"]