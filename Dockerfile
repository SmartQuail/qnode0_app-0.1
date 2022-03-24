FROM python:3.9-alpine3.13
LABEL maintainer="smartquail.io"

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache git
ARG username=smartquail
ARG password=ms95355672
RUN git clone https://github.com/SmartQuail/qnode0_app-0.1.git

COPY ./requirements.txt /requirements.txt
COPY ./scripts /scripts
COPY ./.env /.env



WORKDIR qnode0_app-0.1/qnode0_app
EXPOSE 8000 443
EXPOSE 25


RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps && \
    apk add build-base  postgresql-dev gcc musl-dev python3-dev linux-headers && \
    apk add libffi-dev build-base py3-cffi py3-cryptography && \
    apk add jpeg-dev   zlib-dev libjpeg build-base  wget  && \
    apk del libressl-dev && \
    apk add busybox-extras && \
    apk add openssl-dev && \
    #/py/bin/pip install  rust  &&  \
    #/py/bin/pip install   py3-kiwisolver &&  \
    /py/bin/pip install -r /requirements.txt && \
    apk del openssl-dev  &&  \
    apk add libressl-dev  && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home qnode0 && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R qnode0:qnode0 /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER qnode0

CMD ["run.sh"]
CMD ["gunicorn", "--bind", ":9000", "--workers", "3", "qnode0_app.wsgi:application"]