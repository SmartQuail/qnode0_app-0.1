FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="smartquail.io"

COPY ./ssl/qnode0_app.crt /etc/nginx/ssl/qnode0_app.crt
COPY ./ssl/qnode0_app.key /etc/nginx/ssl/qnode0_app.key
COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh


ENV LISTEN_PORT=8000
ENV NGINX_PROXY=http://qnode0_app:8000
ENV APP_HOST=qnode0_app
ENV APP_PORT=9000

USER root

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static

USER nginx
#ENTRYPOINT [ "/entrypoint.sh" ]
CMD ["/run.sh"]