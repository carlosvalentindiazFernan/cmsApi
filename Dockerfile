FROM python:3.7-alpine as alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apk update                                  \
    && apk add --no-cache                       \
                       curl                     \
                       bash                     \
                       postgresql               \
                       gettext                  \
    && apk add --no-cache --virtual .build-deps \
                       zlib                     \
                       libpq                    \
                       gcc                      \
                       postgresql-dev           \
                       python3-dev              \
                       git                      \
                       musl-dev                 \
                       libffi-dev               \
                       # Pillow deps
                       jpeg-dev                 \
                       zlib-dev                 \
                       freetype-dev             \
                       lcms2-dev                \
                       openjpeg-dev             \
                       tiff-dev                 \
                       tk-dev                   \
                       tcl-dev                  \
                       harfbuzz-dev             \
                       fribidi-dev              \
    && pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install --no-cache-dir -r requirements.txt \
    && apk --purge del .build-deps

# Copy entrypoint and start
COPY ./docker-entrypoint-local.sh /docker-entrypoint-local.sh
RUN chmod 755 /docker-entrypoint-local.sh

# expose the port 8000
EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint-local.sh"]
